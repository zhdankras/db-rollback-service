import os
import time
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from mysql.connector import connect, Error
from clean_and_migrate import cleanup_and_migration_request
from clean_and_migrate import get_status_pipeline
from auth_users_repository import AuthUsers
from accounts_repository import Accounts
from users_repository import Users
from projects_repository import Projects

app = App(token=os.environ.get('SLACK_BOT_TOKEN'))

@app.command("/db-rollback-service")
def handler(ack, body, client):
    ack()

    channel = 'C04KFUH2Q30' 

    if body['channel_id'] == channel:

        client.chat_postMessage(channel=channel, text=f"<@{body['user_id']}> launched the service!")
    
        try:

            client.chat_postMessage(channel=channel, text="INFO: Database connection!")
            mysql_connection = connect(
                host=os.environ.get('HOST_NAME'),
                user=os.environ.get("DB_USERNAME"),
                password=os.environ.get('DB_PASSWORD'),
                database=os.environ.get('DB_USERNAME')
            )
            client.chat_postMessage(channel=channel, text="INFO: Database connection was successful!")

        except Error as e:
            client.chat_postMessage(channel=channel, text=f"ERROR: Database connection failed: {e}")

        # cleaning and migration
        response_message = cleanup_and_migration_request()

        if response_message != None:

            client.chat_postMessage(channel=channel, text=f"INFO: Triggered pipeline with {response_message['id']} and url {response_message['web_url']}")

            while True:

                status_pipeline = get_status_pipeline(response_message['id'])
                client.chat_postMessage(channel=channel, text=f"INFO: Clean and migrate. Pipeline id: {status_pipeline['id']}, status: {status_pipeline['status']}")

                if (status_pipeline['status'] == 'running' or status_pipeline['status'] == 'pending' or 
                    status_pipeline['status'] == 'preparing' or status_pipeline['status'] == 'waiting_for_resource' or 
                    status_pipeline['status'] == 'created'):

                    # timeout
                    time.sleep(15)
                    
                else:

                    if status_pipeline['status'] == 'success':
                        
                        client.chat_postMessage(channel=channel, text="WARNING: The service will load data 60 seconds after cleaning and migrate. ")

                        # timeout
                        time.sleep(60)

                        # insert data
                        client.chat_postMessage(channel=channel, text=AuthUsers(mysql_connection).insert_auth_users())
                        client.chat_postMessage(channel=channel, text=Accounts(mysql_connection).insert_accounts())
                        client.chat_postMessage(channel=channel, text=Projects(mysql_connection).insert_projects())
                        client.chat_postMessage(channel=channel, text=Users(mysql_connection).insert_users())
                    
                    break
        
        else:
            client.chat_postMessage(channel=channel, text="ERROR: Clean and migrate.")

    else: 
        client.chat_postMessage(channel=body['user_id'], text="Calling this command works only in a specific channel.")


if __name__ == "__main__":
    SocketModeHandler(app, os.environ.get('SLACK_APP_TOKEN')).start()

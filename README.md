# Database rollback service
## Service. How it works?
The service performs the following functions:
1. Database(**overhull-dev**) cleanup;
2. Migrates tables by sending a post request to Pipelines API;
3. Adds data to tables(**auth_users**, **accounts**, **users**, **projects**)

The service is integrated with the Slack application. This means that you can use the functionality of the service with the slash command Slack. Since Slaсk applications can use socket mode, the service will work properly.

## Service. Instruction
1. You must be added to the **proj-jlab-kajun-dev-db-rollback** channel on Slack;
2. Go to this channel and then type "/" in the chat. You will see a dropdown list of various commands and built-in applications. From this
dropdown you need **/db-rollback-service**:
<p align="center"><img width="302" alt="Screenshot 2024-04-01 at 2 52 35 PM" src="https://github.com/zhdankras/db-rollback-service/assets/55245041/bb59f6f5-f48b-42d9-889a-35b1a1520365"></p>
3. Click on this application;<br/>
4. If everything went well, you should see logs in this chat:
<p align="center"><img width="768" alt="Screenshot 2024-04-01 at 3 11 55 PM" src="https://github.com/zhdankras/db-rollback-service/assets/55245041/1359e6af-6f14-474e-b3a0-6e1df6d21385"></p>
5. In addition to the logs, you may receive an error(**dispatch_failed**) message related to the long processing time. Ignore it, the service will do its job, and this bug will be fixed soon;<br/>
6. The service will complete its work within a minute. Next, you can check the operation of the service, look at the overhull-dev database. It must go through 3 stages, which were described above. Cleaning, migration, filling tables(auth_users, accounts, users, projects).

# sqlite_rsm
A Replicated State Machine to maintain some SQLite database docker containers

Using Paxos, this application will serve requests for several different db schemas

## Roadmap

1. implement paxos in c#
2. implement the web interface so that my other sites can replace their local .sqlite3 files with RPC's to this site
3. Add functionality to upload new schemas

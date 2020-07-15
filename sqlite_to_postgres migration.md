# Migration of SQLite db to Postgresql
Guide for migrating the `recipes.db` sqlite db to local postgres, and then heroku.

## Docker psql:
Pull:

    docker pull postgres

Start with port 5432 & persistent storage:

    docker run --rm --name pg-docker -e POSTGRES_PASSWORD=tempass -d -p 5432:5432 -v /local/dir/for/permanent/files/:/var/lib/postgresql/data  postgres

With the hostname: `host.docker.internal` and ip: `5432`.

## Docker pg-admin:
Pull:

    docker pull dpage/pgadmin4

Start the container:

    docker run -p 80:80 ^
        -e "PGADMIN_DEFAULT_EMAIL=email@gmail.com"  ^
        -e "PGADMIN_DEFAULT_PASSWORD=tempass" ^
        -d dpage/pgadmin4

Details for docker psql:

    host: host.docker.internal
    database: postgres
    user: postgres
    password: tempass

## pgloader:
`pgload.load` file:

    load database  
        from 'recipes.db'  
        into postgresql://postgres:tempass@host.docker.internal/recipes

    with reset sequences, create no tables, include no drop, create no indexes, disable triggers
    set work_mem to '200MB', maintenance_work_mem to '512 MB';

Docker command to migrate:

    docker pull dimitri/pgloader
    docker run --rm --name pgloader -v /local/dir/for/load/file/and/db/:/data dimitri/pgloader:latest pgloader /data/pgload.load


## Dump psql db into file:
Dump postgres database into backup file:

    docker exec pg-docker sh -c "PGPASSWORD=tempass pg_dump -Fc --no-acl --no-owner -h localhost -U postgres recipes > /var/lib/postgresql/data/recipes.dump"

This should generate a `recipes.dump` file under `/local/dir/for/permanent/files/` that was set when the `pg-docker` container was run.

## Upload dump file to Heroku postgres:
The file needs to be uploaded to a site where a URL can be generated.
Then:

    heroku pg:backups:restore "DUMP_FILE_URL" DATABASE_URL --app app-name
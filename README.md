# bottir 

<em>Not so flexible certbot wrapper mainly for my personal use</em>

**Usage:** 

    python3 main.py -e user@email.com -d whatever.domain.com -k awsaccesskey -s awssecret
additionally:

    -t or --test (generates staging certificates)
    -p or --pfx (converts certificate into pfx because Azure is annoying)
    -v or --validate-pfx (validates the pfx, gives some output)

There is the requirements.txt file for the dependencies, if you need to.

That's it. 


# Setting up a Database Project:

## SYSTEM-WIDE SETUP:

### Install postgresql:
First, you will need to install PostgreSQL on your machine. You can do this using Homebrew on macOS. Here, we're using PostgreSQL 15 but if there's a newer release you're asked to use, just substitute in that version number instead:

```
# Install postgresql.
$ brew install postgresql@15
```
Once installed, you'll need to make sure that installation directory is on your PATH environment variable. In the output from the Homebrew installation you just ran, should be a line which looks like this one, which you should copy, paste into the terminal and run:

```
echo 'export PATH="/opt/homebrew/opt/postgresql@15/bin:$PATH"' >> ~/.zshrc
```

Afterwards, either start a new terminal session or just run `zsh`.

```
# Run this after the installation
# to start the postgresql software
# in the background.
$ brew services start postgresql@15

# You should get the following output:
==> Successfully started `postgresql@15` (label: homebrew.mxcl.postgresql@15)
```

<hr>


## 0) PSQL PROJECT SET UP:

```
$ psql -h 127.0.0.1

psql (15.2)
Type "help" for help.

leoht=# 
```

### Getting an error?

If you get an error similar to `connection to server at "127.0.0.1", port 5432 failed: FATAL: database "leoht" does not exist` - you can use the `createdb command` to create the default database psql tries to connect to, which is named after your macOS system username.

For example, my macOS username is `leoht`, so I'd run the bash command: `createdb leoht` - this should fix the connection error.

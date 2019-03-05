#! /usr/bin/env bash

# Register current dir int sys.path
export PYTHONPATH="."

case "$1" in
    run)
        python src/server/main.py
        ;;
    migrate)
        case "$2" in
            gen)
                echo "Generate a miration with comment: ${@:3}"
                read -rsn1 -p"Press any key to continue"; echo
                alembic revision --autogenerate -m "${@:3}"
                ;;
            upgrade)
                echo "Upgrade head"
                alembic upgrade head
                ;;
            *)
                echo "Usage: $0 $1 {gen|upgrade}"
                exit 1
        esac
        ;;
    *)
        echo "Usage: $0 {run|migrate}"
        exit 1
esac

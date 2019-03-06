#! /usr/bin/env bash
# Usage: ./make.sh <command> [<subcommand>]

# Register current dir int sys.path
export PYTHONPATH="."

case "$1" in
    # cmd: run
    run)
        python src/server/main.py
        ;;
    migrate)
        case "$2" in
            # cmd: migrate gen
            gen)
                echo "Generate a miration with comment: ${@:3}"
                read -rsn1 -p"Press any key to continue"; echo
                alembic revision --autogenerate -m "${@:3}"
                ;;
            # cmd: migrate upgrade
            upgrade)
                echo "Upgrade head"
                alembic upgrade head
                ;;
            *)
                echo "Usage: $0 $1 {gen|upgrade}"; exit 1
        esac
        ;;
    *)
        echo "Usage: $0 {run|migrate}"; exit 1
esac

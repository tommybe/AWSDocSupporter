from flask import Flask
import click

flask_app = Flask(__name__)

def run_ml_trigger(
    flask_host: str = "127.0.0.1",
    flask_port: int = 5000
) -> NoReturn:
    trigger = MLTrigger(min_retraining_days, pg_connection_string, org_code, min_queue_len, min_rerun_period)
    flask_app.add_url_rule("/get_shot_id", "get_shot_id", trigger.assign_new_shot_id)
    flask_app.add_url_rule("/get_shot_type/<shot_id>", "get_shot_type", trigger.assign_shot_type)
    flask_app.add_url_rule("/get_org_code", "get_org_code", trigger.assign_org_code)
    flask_app.add_url_rule("/get_user/<shot_id>", "get_user", trigger.assign_user_for_training)
    # TODO: Parametrize debug parameter in case of problems to be able to trace it back. TASK REQUIRED
    Thread(target=flask_app.run, kwargs={"host": flask_host, "port": flask_port, "debug": False}).start()
    trigger.run_eternal_trigger()


@click.command(help="ML Trigger for removing alerting models and updating Postgres table based on training readiness.")
@click.option("--flask_host", type=str, required=True, help="Host for questioning flask server.")
@click.option("--flask_port", type=int, required=True, help="Port for questioning flask server.")
def run(
    flask_host: str,
    flask_port: int,
) -> NoReturn:
    run_ml_trigger(
        flask_host,
        flask_port,
    )


def main():
    run(auto_envvar_prefix="ML_TRIGGER")


if __name__ == "__main__":
    run()
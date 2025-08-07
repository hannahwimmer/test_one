from prefect import task, flow

@task
def get_greeting_text():
    text = "Hey there!"
    return text

@flow
def greeting_procedure():
    greeting_text = get_greeting_text()
    more_text = "Let's check out prefect for workflow management!"
    return greeting_text + " " + more_text


if __name__ == "__main__":
    greeting_procedure()

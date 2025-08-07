from prefect import task, flow
import numpy as np

@task
def get_greeting_text():
    text = "Hey there!"
    value = np.mean([2,5,4])
    return text + " Our value is: " + str(value)

@flow
def greeting_procedure():
    greeting_text = get_greeting_text()
    more_text = "Let's check out prefect for workflow management!"
    return greeting_text + " " + more_text


if __name__ == "__main__":
    greeting_procedure()

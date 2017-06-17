from flask import Flask, render_template
from flask_ask import Ask, statement, question, session
from openweather import find_weather

import json
app = Flask(__name__)
ask = Ask(app, "/")

@ask.launch

def new_ask():
    welcome = render_template('welcome')
    empty = render_template('empty')
    return question(welcome).reprompt(empty)

@ask.intent('SearchWeatherIntent')
def search_weather(query):
    if not query:
        empty_query = render_template('empty')
        return question(empty_query)

    weather = find_weather(query)

    results = render_template('results')

    session.attributes['result'] = weather
    session.attributes['index'] = 0

    return question(results)

@ask.intent('AMAZON.YesIntent')
def show_result():
    results = session.attributes['result']
    result = render_template('weather_update', temperature = results.data.main.temp)
    return question(result)

@ask.intent('AMAZON.NoIntent')
def close():
    result = render_template('exit')
    return statement(result)

@ask.intent('AMAZON.HelpIntent')
def help():
    result = render_template('help')
    return question(result)

@ask.intent('AMAZON.StopIntent')
def stop():
    result = render_template('bye')
    return statement(result)

@ask.intent('AMAZON.CancelIntent')
def stop():
    result = render_template('bye')
    return statement(result)



if __name__ == '__main__':
    app.run(debug=True)
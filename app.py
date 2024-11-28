# import neccesary libaries
import streamlit as st
import random
import json
import requests
from geopy.distance import geodesic
from statistics import mean

# initialize a dictionary with a key for every country and it's coordinates as it's value.
country_dict = {'Afghanistan': (33.93911, 67.709953), 'Albania': (41.153332, 20.168331), 'Algeria': (28.033886, 1.659626), 'Andorra': (42.506285, 1.521801), 'Angola': (-11.202692, 17.873887), 'Antigua and Barbuda': (17.060816, -61.796428), 'Argentina': (-38.416097, -63.61667199999999), 'Armenia': (40.069099, 45.038189), 'Australia': (-25.274398, 133.775136), 'Austria': (47.516231, 14.550072), 'Azerbaijan': (40.143105, 47.576927), 'Bahamas': (25.03428, -77.39627999999999), 'Bahrain': (26.0667, 50.5577), 'Bangladesh': (23.684994, 90.356331), 'Barbados': (13.193887, -59.543198), 'Belarus': (53.709807, 27.953389), 'Belgium': (50.503887, 4.469936), 'Belize': (17.189877, -88.49765), 'Benin': (9.30769, 2.315834), 'Bhutan': (27.514162, 90.433601), 'Bolivia': (-16.290154, -63.58865299999999), 'Bosnia and Herzegovina': (43.915886, 17.679076), 'Botswana': (-22.328474, 24.684866), 'Brazil': (-14.235004, -51.92528), 'Brunei': (4.535277, 114.727669), 'Bulgaria': (42.733883, 25.48583), 'Burkina Faso': (12.238333, -1.561593), 'Burundi': (-3.373056, 29.918886), 'Cape Verde': (16.5388, -23.0418), 'Cambodia': (12.565679, 104.990963), 'Cameroon': (7.369721999999999, 12.354722), 'Canada': (56.130366, -106.346771), 'Central African Republic': (6.611110999999999, 20.939444), 'Chad': (15.454166, 18.732207), 'Chile': (-35.675147, -71.542969), 'China': (35.86166, 104.195397), 'Colombia': (4.570868, -74.297333), 'Comoros': (-11.6455, 43.3333), 'Congo': (-0.228021, 15.827659), 'Costa Rica': (9.748917, -83.753428), 'Croatia': (45.1, 15.2000001), 'Cuba': (21.521757, -77.781167), 'Cyprus': (35.126413, 33.429859), 'Czech Republic': (49.81749199999999, 15.472962), 'Denmark': (56.26392, 9.501785), 'Djibouti': (11.825138, 42.590275), 'Dominica': (15.414999, -61.37097600000001), 'Dominican Republic': (18.735693, -70.162651), 'Ecuador': (-1.831239, -78.18340599999999), 'Egypt': (26.820553, 30.802498), 'El Salvador': (13.794185, -88.89653), 'Equatorial Guinea': (1.650801, 10.267895), 'Eritrea': (15.179384, 39.782334), 'Estonia': (58.595272, 25.0136071), 'Eswatini': (26.5225, 31.4659), 'Ethiopia': (9.145, 40.489673), 'Fiji': (-17.713371, 178.065032), 'Finland': (61.92410999999999, 25.7481511), 'France': (46.227638, 2.213749), 'Gabon': (-0.803689, 11.609444), 'Gambia': (13.443182, -15.310139), 'Georgia': (32.1656221, -82.9000751), 'Germany': (51.165691, 10.451526), 'Ghana': (7.946527, -1.023194), 'Greece': (39.074208, 21.824312), 'Grenada': 
(12.1165, -61.67899999999999), 'Guatemala': (15.783471, -90.230759), 'Guinea': (9.945587, -9.696645), 'Guinea-Bissau': (11.803749, -15.180413), 'Guyana': (4.860416, -58.93018), 'Haiti': (18.971187, -72.285215), 'Honduras': (15.199999, -86.241905), 'Hungary': (47.162494, 19.5033041), 'Iceland': (64.963051, -19.020835), 'India': (20.593684, 78.96288), 'Indonesia': (-0.789275, 113.921327), 'Iran': (32.427908, 53.688046), 'Iraq': (33.223191, 43.679291), 'Ireland': (53.1423672, -7.692053599999999), 'Israel': (31.046051, 34.851612), 'Italy': (41.87194, 12.56738), 'Jamaica': (18.109581, -77.297508), 'Japan': (36.204824, 138.252924), 'Jordan': (30.585164, 36.238414), 'Kazakhstan': (48.019573, 66.923684), 'Kenya': (-0.023559, 37.906193), 'Kiribati': (-3.370417, -168.734039), 'Kuwait': (29.31166, 47.481766), 
'Kyrgyzstan': (41.20438, 74.766098), 'Laos': (19.85627, 102.495496), 'Latvia': (56.879635, 24.603189), 'Lebanon': (33.854721, 35.862285), 'Lesotho': (-29.609988, 28.233608), 'Liberia': (6.428055, -9.429499000000002), 'Libya': (26.3351, 17.228331), 'Liechtenstein': (47.166, 9.555373), 'Lithuania': (55.169438, 23.881275), 'Luxembourg': (49.815273, 6.129582999999999), 'Madagascar': (-18.766947, 46.869107), 'Malawi': (-13.254308, 34.301525), 'Malaysia': (4.210484, 101.975766), 'Maldives': (3.202778, 73.22068), 'Mali': (17.570692, -3.996166), 'Malta': (35.937496, 14.375416), 'Marshall Islands': (7.131474, 171.184478), 'Mauritania': (21.00789, -10.940835), 'Mauritius': (-20.348404, 57.55215200000001), 'Mexico': (23.634501, -102.552784), 'Micronesia': (7.425554, 150.550812), 'Moldova': (47.411631, 28.369885), 'Monaco': (43.73841760000001, 7.424615799999999), 'Mongolia': (46.862496, 103.846656), 'Montenegro': (42.708678, 19.37439), 'Morocco': (31.791702, -7.092619999999999), 'Mozambique': (-18.665695, 35.529562), 'Myanmar': (21.916221, 95.955974), 'Namibia': (-22.95764, 18.49041), 'Nauru': (-0.522778, 166.931503), 'Nepal': (28.394857, 84.12400799999999), 'Netherlands': (52.132633, 5.291265999999999), 'New Zealand': (-40.900557, 174.885971), 'Nicaragua': (12.865416, -85.207229), 'Niger': (17.607789, 8.081666), 'Nigeria': (9.081999, 8.675277), 'North Korea': (40.339852, 127.510093), 'North Macedonia': (41.608635, 21.745275), 'Norway': (60.47202399999999, 8.468945999999999), 'Oman': (21.4735329, 55.975413), 'Pakistan': (30.375321, 69.34511599999999), 'Palau': (7.514979999999999, 134.58252), 'Panama': (8.537981, -80.782127), 'Papua New Guinea': (-6.314992999999999, 143.95555), 'Paraguay': (-23.442503, -58.443832), 'Peru': (-9.189967, -75.015152), 'Philippines': (12.879721, 121.774017), 'Poland': (51.919438, 19.145136), 'Portugal': (39.39987199999999, -8.224454), 'Qatar': (25.354826, 51.183884), 'Romania': (45.943161, 24.96676), 'Russia': (61.52401, 105.318756), 'Rwanda': (-1.940278, 29.873888), 'Saint Kitts and Nevis': (17.357822, -62.782998), 'Saint Lucia': (13.909444, -60.978893), 'Saint Vincent and the Grenadines': (12.984305, -61.287228), 'Samoa': (-13.759029, -172.104629), 'San Marino': (43.94236, 12.457777), 'Sao Tome and Principe': (0.18636, 6.613080999999999), 'Saudi Arabia': (23.885942, 45.079162), 'Senegal': (14.497401, -14.452362), 'Serbia': (44.016521, 21.005859), 'Seychelles': (-4.679574, 55.491977), 'Sierra Leone': (8.460555, -11.779889), 'Singapore': (1.352083, 103.819836), 'Slovakia': (48.669026, 19.699024), 'Slovenia': (46.151241, 14.995463), 'Solomon Islands': (-9.64571, 160.156194), 'Somalia': (5.152149, 46.199616), 'South Africa': (-30.559482, 
22.937506), 'South Korea': (35.907757, 127.766922), 'South Sudan': (6.876991899999999, 31.3069788), 'Spain': (40.46366700000001, -3.74922), 'Sri Lanka': (7.873053999999999, 80.77179699999999), 'Sudan': (12.862807, 30.217636), 'Suriname': (3.919305, -56.027783), 'Sweden': (60.12816100000001, 18.643501), 'Switzerland': (46.818188, 8.227511999999999), 'Syria': (34.80207499999999, 38.996815), 'Tajikistan': (38.861034, 71.276093), 'Tanzania': (-6.369028, 34.888822), 'Thailand': (15.870032, 100.992541), 'Timor-Leste': (-8.874217, 125.727539), 'Togo': (8.619543, 0.824782), 'Tonga': (-21.178986, -175.198242), 'Trinidad and Tobago': (10.691803, -61.222503), 'Tunisia': (33.886917, 9.537499), 'Turkey': (38.963745, 35.243322), 'Turkmenistan': (38.969719, 59.556278), 'Tuvalu': (-7.109534999999999, 177.64933), 'Uganda': (1.373333, 32.290275), 'Ukraine': (48.379433, 31.1655799), 'United Arab Emirates': (23.424076, 53.847818), 'United Kingdom': (55.378051, -3.435973), 'United States': (40.7605367, -73.9788903), 'Uruguay': (-32.522779, -55.765835), 'Uzbekistan': (41.377491, 64.585262), 'Vanuatu': (-15.376706, 166.959158), 'Vatican City': (41.902916, 12.453389), 'Venezuela': (6.42375, -66.58973), 'Vietnam': (14.058324, 108.277199), 'Yemen': (15.552727, 48.516388), 'Zambia': (-13.133897, 27.849332), 'Zimbabwe': (-19.015438, 29.154857)}

# initialize a list of all countries
countries = list(country_dict.keys())

# Function to calculate distance takes two country names and return float distance
def calculate_distance(country1, country2):
    # Retrieve the coordinates of the two countries
    coords1 = country_dict[country1]
    coords2 = country_dict[country2]
    
    # Calculate the distance
    distance = geodesic(coords1, coords2).kilometers

    # return the distance
    return distance

# Function to takes two countries and returns a string estimate of it's distance 
def calculate_distance_est(country1, country2):
    
    # Calculate the distance
    distance = calculate_distance(country1, country2)

    # check and return different strings for different ranges
    if (distance < 500):
        return "less than 500km away"
    elif (distance > 500 and distance < 1000):
        return "between 500km and 1000km away"
    elif (distance > 1000 and distance < 2000):
        return "between 1000km and 2000km away"
    elif (distance > 2000 and distance < 5000):
        return "between 2000km and 5000km away"
    else:
        return "more than 5000km away"

# chat function that takes a string and outputs a string response from gemini 1.5 flash (own backend)
def chat(message):

    # construct the body
    body = json.dumps({
        'conversation_history': [{'role': 'user', 'text': message}],
    })

    # set the url and header
    url = 'https://vertex-backend-607079336624.europe-west4.run.app/chat'
    headers = {
        'Content-Type': 'application/json',
    }

    try:
        # send the request
        response = requests.post(url, headers=headers, data=body)
        if response.status_code == 200:
            response_data = response.json()
            original_string = response_data.get('response', '')
            # return the result
            return original_string
        else:
            print(f'Failed with status code: {response.status_code}')
            print(f'Response body: {response.text}')
            return None
    except Exception as e:
        # catch potential erros
        print(f'Error: {e}')
        return None

# function to reset the game
def reset():

    # set a new random country to the goal
    random_index = random.randint(0,len(countries)-1)
    st.session_state.goal = countries[random_index]
    
    # reset all game variables

    st.session_state.score = 0

    st.session_state.question = ""

    st.session_state.questions = []

    st.session_state.guesses = []

    st.session_state.guess = "Select"

    st.session_state.finished = False

    st.session_state.error = False

    st.session_state.hints = []

# function that adds a hint
def hint():
    # check if it's the first hint and get a small hint
    if len(st.session_state.hints) == 0:
        response = chat(f'We are playing a country guessing, the country in question is {st.session_state.goal}, give a small hint that does not reveal too much to what the country could be to the user and which is not in the following: {st.session_state.hints}')
    # check if it's the second hint and get a median hint
    elif len(st.session_state.hints) == 1:
        response = chat(f'We are playing a country guessing, the country in question is {st.session_state.goal}, give a median hint that does not reveal too much to what the country could be to the user and which is not in the following: {st.session_state.hints}')
    # check if it's a third or later hint and get a big hint
    else:
        response = chat(f'We are playing a country guessing, the country in question is {st.session_state.goal}, give a big hint to what the country could be to the user and which is not in the following: {st.session_state.hints}')

    # add the hint to the hints list
    st.session_state.hints.append(response)

    # increase the score by 3 
    st.session_state.score += 3

# function to ask a question takes a string question and updates the questions list
def ask_question():

    # construct prompt
    response = chat(f'We are playing a country guessing, the country in question is {st.session_state.goal}, answer the following question: {st.session_state.question}, answer this question strictly with either yes or no')
    
    # check if the api call succeeded
    if response == None:
        st.session_state.error = True
    else:
        # increace the score by 1
        st.session_state.score += 1

        # add the question and the response to the list of questions (if it isn't empty)
        if st.session_state.question.strip():
            st.session_state.questions.append(f'{st.session_state.question}: {response.lower()}')
            st.session_state.question = ""

# functions that makes a guess and changes the state accordingly
def make_guess():
    # check if there is actually a country selected
    if st.session_state.guess != 'Select' and not st.session_state.finished:
        # check if the guess is correct
        if st.session_state.guess == st.session_state.goal:
            # add the score to the scores list
            st.session_state.scores.append(st.session_state.score)

            # show balloons
            st.balloons()

            # set the game state to finished
            st.session_state.finished = True

            # update the distance lists
            st.session_state.distances.extend(st.session_state.current_distances)
            st.session_state.current_distances= []

            # set the highscore
            if st.session_state.highscore == -1:
                st.session_state.highscore = st.session_state.score
            elif st.session_state.highscore > st.session_state.score:
                st.session_state.highscore = st.session_state.score
        else:
            # check if the user already guessed the country
            if st.session_state.guess in st.session_state.guesses:
                st.write(f"You have already guesses: {st.session_state.guess} try something else")
            else:
                # add the guess to the list of guesses
                st.session_state.guesses.append(st.session_state.guess)

                # add the distance to the list of distances
                st.session_state.current_distances.append(calculate_distance(st.session_state.guess, st.session_state.goal))
                
                # increase the score by 2
                st.session_state.score += 2

# initialize the goal by taking a random index over the
if 'goal' not in st.session_state:
    random_index = random.randint(0,len(countries)-1)
    st.session_state.goal = countries[random_index]
    print(st.session_state.goal)

# initialze the other variables
    
if 'score' not in st.session_state:
    st.session_state.score = 0

if 'question' not in st.session_state:
    st.session_state.question = ""

if 'questions' not in st.session_state:
    st.session_state.questions = []

if 'guesses' not in st.session_state:
    st.session_state.guesses = []

if 'guess' not in st.session_state:
    st.session_state.guess = "Select"

if 'highscore' not in st.session_state:
    st.session_state.highscore = -1

if 'finished' not in st.session_state:
    st.session_state.finished = False

if 'error' not in st.session_state:
    st.session_state.error = False

if 'scores' not in st.session_state:
    st.session_state.scores = []

if 'distances' not in st.session_state:
    st.session_state.distances = []

if 'current_distances' not in st.session_state:
    st.session_state.current_distances = []

if 'hints' not in st.session_state:
    st.session_state.hints = []

# show the page controller
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Play", "Stats"])

# check if the play page is selected and show it
if page == "Play":

    # desribe and explain the game
    st.title("The country guessing game")
        
    st.write("A random country is selected and you can ask yes or no questions about the country to an AI. Every question adds 1 point, every wrong guess 2 and every hint 3. Try to finish with the lowest score")

    st.write("### Ask a yes or no question about the country")

    # have a text input for asking questions and call the ask question function when something
    st.text_input(label=' ', max_chars=200,label_visibility='collapsed', key="question", on_change=ask_question)

    # display the asked questions in reverserd order (last asked on the top)
    for asked_question in st.session_state.questions[::-1]:
        st.write(f"- {asked_question}")

    # display button that will add a hint
    st.button(label="Get a hint", on_click=hint)

    # display the hints in reverserd order (last asked on the top)
    for hint in st.session_state.hints[::-1]:
        st.write(f"- {hint}")

    st.write("### Guess a country")

    # show selection box with all countries and run the make guess function when a guess is made
    st.selectbox(label=' ',label_visibility='collapsed', options= ['Select'] + countries, key='guess', on_change=make_guess)

    # display an error if there is an error
    if st.session_state.error:
        st.write(f"### An error occured this is likely due to the daily api limit has been exceeded")
    
    # check if the game is finished
    if st.session_state.finished:

        # display the game results and play again button
        st.write(f"### {st.session_state.goal} was correct! your final score is {st.session_state.score} guesses")
        st.button(label="Play again", on_click=reset)

    # display the guesses in reverserd order (last asked on the top)
    for guess in st.session_state.guesses[::-1]:
        # check if the game is finished
        if st.session_state.finished:
            # display the actual distance
            st.write(f"- {guess} was incorrect, the target country was {round(calculate_distance(guess, st.session_state.goal))} km away")
        else:
            # display an estimation of the distance
            st.write(f"- {guess} was incorrect, the target country is {calculate_distance_est(guess, st.session_state.goal)}")

    # display the current score
    score = f"Your current score is {st.session_state.score}"

    # if there is a highscore display the highscore
    if st.session_state.highscore != -1:
        score += f". Your high score is {st.session_state.highscore}"
    st.write(f'### {score}')

# check if the stats page is selected and show it
elif page == "Stats":
    st.title("Game Analytics")

    # check if there are any scores
    if st.session_state.scores:
        # display high score, average score, amount of games, the average distance of a guess and the last score
        st.write(f"### High Score: {min(st.session_state.scores)}")
        st.write(f"### Average Score: {sum(st.session_state.scores) / len(st.session_state.scores)}")
        st.write(f"### Total Games Played: {len(st.session_state.scores)}")
        if st.session_state.distances:
            st.write(f"### Average distance between guess and target: {round(mean(st.session_state.distances))}")
        st.write(f"### Last Score: {st.session_state.scores[-1]}")
    else:
        st.write("No games played yet. Play a game to see analytics.")
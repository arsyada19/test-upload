from PyQt5.QtCore import QTime

win_x, win_y = 100, 200
win_width, win_height = 1000, 600

txt_hello = 'Welcome to the Health status detection program!'
txt_next = 'Start'
text_instruction = ('This application allows you to use the Rufier test to make an initial diagnosis of your health.\n'
                    'The Rufier test is a set of physical exercises designed to assess your cardiac performance during physical exertion.\n'
                    'The subject lies in the supine position for 5 minutes and has their pulse rate measured for 15 seconds;\n'
                    'then, within 45 seconds, the subject performs 30 squats.\n'
                    'When the exercise ends, the subject lies down and their pulse is measured again for the first 15 seconds\n'
                    'and then for the last 15 seconds of the first minute of the recovery period.\n'
                    'Important! If you feel unwell during the test (dizziness,\n'
                    'tinnitus, shortness of breath, etc.), stop the test and consult a physician.')
txt_title = 'Health'
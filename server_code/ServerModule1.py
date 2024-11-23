import anvil.email
import anvil.server

@anvil.server.callable
def send_feedback(name, email, feedback):
  # Send yourself an email each time feedback is submitted
  anvil.email.send(to="zrundle@una.edu", # Change this to your email address!
                   subject=f"Feedback from {name}",
                   text=f"""
                   
  A new person has filled out the feedback form!

  Name: {name}
  Email address: {email}
  Feedback:
  {feedback}
  """)

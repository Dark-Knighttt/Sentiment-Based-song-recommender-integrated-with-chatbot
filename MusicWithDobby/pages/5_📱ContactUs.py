import streamlit as st

from email.message import EmailMessage
import smtplib
import getpass

st.set_page_config(
    page_icon="🎧",
    page_title="MusicChatMate",
    layout="wide",
    # initial_sidebar_state="expanded",
)

st.title("Contact Us")

# Collect user data
user_name = st.text_input("Enter your name:")
user_email = st.text_input("Enter your email address:")
user_message = st.text_area("Enter your message:")

# Create contact form
# if st.button("Submit"):
    # with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    #     print('mai chala')
    #     server.login(getpass.getpass("Enter your Gmail address:"), getpass.getpass("Enter your Gmail password:"))

    #     # Send email to recipient
    #     email = EmailMessage()
    #     email["Subject"] = f"Message from {user_name}"
    #     email["From"] = user_email
    #     email["To"] = "thakregauri3011@gmail.com" # Replace with the email address of the recipient
    #     email.set_content(user_message)
    #     server.send_message(email)

    # st.write("Thank you for reaching out to us! We will get back to you soon.")

if st.button("Submit"):
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        print('mai chala')
        server.login(user_email, getpass.getpass("Enter your Gmail password:"))

        # Send email to recipient
        email = EmailMessage()
        email["Subject"] = f"Message from {user_name}"
        email["From"] = user_email
        email["To"] = "thakregauri3011@gmail.com" # Replace with the email address of the recipient
        email.set_content(user_message)
        server.send_message(email)
# ----------------------------------------------------------------------

# import streamlit as st
# import smtplib
# from email.message import EmailMessage

# def send_email(name, email, message):
#     # Set up the email content
#     msg = EmailMessage()
#     msg.set_content(f"From: {name}\nEmail: {email}\n\n{message}")
#     msg['Subject'] = 'Message from Contact Us Form'
#     msg['From'] = 'your_email@gmail.com'  # Replace with your email
#     msg['To'] = 'destination@example.com'  # Replace with the destination email

#     # Connect to an SMTP server and send the email
#     with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
#         smtp.starttls()
#         smtp.login('your_email@gmail.com', 'your_password')  # Replace with your email credentials
#         smtp.send_message(msg)

# def contact_form():
#     st.title("Contact Us")
#     st.write("Please fill in the form below to get in touch.")

#     name = st.text_input("Name")
#     email = st.text_input("Email")
#     message = st.text_area("Message", height=200)

#     if st.button("Submit"):
#         send_email(name, email, message)
#         st.success(f"Thank you, {name}! Your message has been sent to our team. We'll contact you at {email} shortly.")

# if __name__ == '__main__':
#     contact_form()



# ------------------------------------------------------------

# import streamlit as st

# def main():
#     st.title('Contact Us')
#     st.write('Feel free to reach out to us!')

#     name = st.text_input('Your Name', max_chars=50)
#     email = st.text_input('Your Email', max_chars=50)
#     message = st.text_area('Your Message', max_chars=200)

#     submitted = st.button('Submit')

#     if submitted:
#         if name and email and message:
#             # Process the submitted data (you can add your own logic here)
#             st.success('Mail Sent!')
#         else:
#             st.error('Please fill in all the fields.')

# if __name__ == "__main__":
#     main()
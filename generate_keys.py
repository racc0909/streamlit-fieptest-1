import pickle
from pathlib import Path

import streamlit_authenticator as stauth
from streamlit_authenticator.utilities.hasher import Hasher

names = ["Peter Parker", "Rebecca Miller"]
usernames = ["pparker", "rmiller"]
passwords = ["abc123", "def456"]

#bcrypt for hashing
hashed_passwords = stauth.Hasher(passwords).generate()


file_path = Path(__file__).parent / "hashed_pw.pk1"
with file_path.open("wb") as file:
  pickle.dump(hashed_passwords, file)

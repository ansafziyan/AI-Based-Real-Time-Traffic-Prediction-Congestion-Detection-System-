\# 🚦 AI Traffic Prediction System





DESCRIPTION

This project is a machine learning-based traffic prediction system built using deep learning. The model is trained on a dataset and deployed using FastAPI to provide real-time predictions via a REST API.



The system demonstrates end-to-end AI deployment including model training, backend development, and API integration.



FEATURES

\## 🔥 Features

\- Deep Learning Regression Model

\- Real-time Prediction API using FastAPI

\- Trained using Python and TensorFlow

\- REST API with interactive documentation

\- Deployable using Docker and cloud platforms



\## 📁 Project Structure

traffic-ai-project/

│

├── app.py              # Backend API

├── train.py            # Model training script

├── model.h5            # Trained model

├── requirements.txt    # Dependencies



\## ⚙️ INSTALLATION



```bash

pip install -r requirements.txt



\---



\## 📌 RUN PROJECT

```md

\## ▶️ Run the Application



```bash

python -m uvicorn app:app



\---



\## 📌 API USAGE

```md

\## 🌐 API Usage



Open in browser:

http://127.0.0.1:8000/docs



Use the `/predict` endpoint to send input and receive predictions.



\## 🧪 Sample Input



```json

{

&#x20; "input": \[0.1, 0.2, 5, 0, 0.5, 6, 50, 3, 4, 300, 15, 390, 5]

}





\---



\## 📌 TECHNOLOGIES

```md

\## 🛠️ Technologies Used

\- Python

\- TensorFlow

\- FastAPI

\- NumPy



\## 👨‍💻 Author

Made by ANSAF ZIYAN


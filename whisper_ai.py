import whisper

class whisper_ai():

    def __init__(self, model_type="base"):
        self.model_type = model_type

    def load_whisper_model(self):
        # Load the model.
        try:
            print("Downloading the model...")
            self.model = whisper.load_model(self.model_type)
            print("Done downloading the model!")
        except Exception as error:
            raise Exception("Model not found! \n" + str(error))
        return self.model

    def transcribe_audio(self, audio_path):
        # Transcribe the audio file.
        if audio_path == "":
            raise Exception("Error, audio_path is empty")
        try:
            print("Transcribing, please wait...")
            result = self.model.transcribe(audio_path)
        except Exception as error:
            raise Exception("A transcription error occurred when processing the audio file \n " + str(error)) 
        
        return result
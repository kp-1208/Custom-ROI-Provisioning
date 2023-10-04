"""
This module contains the default parameters used by the app
"""

########################################################################################################################
# Parameters specific to Project Paths
########################################################################################################################
# Path where dataset is stored (used for creating face embedding)
DATASET_PATH = "dataset/Full-Dataset"  # Path to new dataset that contains only new images

# The path where InsightFace-REST face encodings are stored
LATEST_ENCODING_PATH = "dataset/insightface_face_encoding.pkl"

# The path where logs will be stored
LOGS_FOLDER = "logs"
MULTICAM_SERVER_LOG_FILE_PATH = f"{LOGS_FOLDER}/multicam_server.log"
DATABASE_SERVER_LOG_FILE_PATH = f"{LOGS_FOLDER}/database_server.log"
API_LOG_FILE_PATH = f"{LOGS_FOLDER}/api.log"
FEEDBACK_LOG_FILE_PATH = f"{LOGS_FOLDER}/feedback.log"
########################################################################################################################


########################################################################################################################
# Parameters specific to Cameras, Livestreams and Buffers
########################################################################################################################
# Frame Rate Factor to drop the frames not needed to process
FRAME_RATE_FACTOR = 3

# Set video frame height and width
FRAME_HEIGHT = 360  # 720 #576
FRAME_WIDTH = 640  # 1280 #1024

# set BATCH_SIZE for face detection
BATCH_SIZE = 64  # for DGX 64, 8 for CPU

# buffer size for video streaming to minimize inconsistent network conditions
LIVE_STREAM_BUFFER_SIZE = 2048  # single camera

# buffer size for frames on which face recognition will be performed
LIVE_STREAM_BUFFER_PURGE_SIZE = 256  # 256 for DGX

# IP Camera Details
IP_CAMS = {
    "tapo-cam": ["rtsp://grilsquad:grilsquad@192.168.15.90:554/stream1", (800, 600, -10, -10)],
    "left": ["rtsp://grilsquad:grilsquad@192.168.15.90:554/stream1", (800, 600, -10, -10)],
    # "right": ["rtsp://grilsquad:grilsquad@192.168.15.90:554/stream1", (800, 600, -10, -10)],
    # "divendra-cam": ["http://192.168.15.1:4747/video", (640, 360, 0, 0)],
    # "anubhav-webcam": ["http://192.168.16.123:5000", (640, 360, 0, 0)],
    # "riya-webcam": ["http://192.168.12.6:5000", (640, 360, 0, 0)],
    # "sugandh-webcam": ["http://192.168.18.167:5000", (640, 360, 0, 0)],
    # "hamza-webcam": ["http://192.168.19.72:5000", (640, 360, 0, 0)],
    # "satya-webcam": ["http://192.168.12.9:5000", (640, 360, 0, 0)],
    # "prakhar-webcam": ["http://192.168.15.40:5000", (640, 360, 0, 0)],
    # "kshitij-rtsp-cam": ["rtsp://admin:admin@192.168.15.2:4747", (640, 360, 0, 0)]
    "hamza-cam": ["http://192.168.15.5:4747/video", (640, 360, 0, 0)],
    # "hamza-cam-3": ["http://192.168.0.115:4747/video", (640, 360, 0, 0)],
    # "hamza-cam-4": ["http://192.168.0.115:4747/video", (640, 360, 0, 0)],
    # "hamza-cam-5": ["http://192.168.0.115:4747/video", (640, 360, 0, 0)],
    # "hamza-cam-6": ["http://192.168.0.115:4747/video", (640, 360, 0, 0)],
    # "hamza-cam-7": ["http://192.168.0.115:4747/video", (640, 360, 0, 0)],
    # "hamza-cam-8": ["http://192.168.0.115:4747/video", (640, 360, 0, 0)],
    # "riya-cam": ["http://192.168.3.202:4747/video", (640, 360, 0, 0)],
    # "satya-cam": ["http://192.168.15.16:4747/video", (640, 360, 0, 0)],
    # "satya-cam-2": ["http://192.168.15.55:4747/video", (640, 360, 0, 0)],
    # "satya-cam-3": ["http://192.168.15.55:4747/video", (640, 360, 0, 0)],
    # "satya-cam-4": ["http://192.168.15.55:4747/video", (640, 360, 0, 0)],
    # "satya-cam-5": ["http://192.168.15.55:4747/video", (640, 360, 0, 0)],
    # "tejveer-cam": ["http://192.168.15.24:4747/video", (640, 360, 0, 0)],
    # "tejveer-cam-2": ["http://192.168.19.151:4747/video", (640, 360, 0, 0)],
    # "tejveer-cam-3": ["http://192.168.19.151:4747/video", (640, 360, 0, 0)]
    # "vedant-cam": ["http://192.168.3.220:4747/video", (640, 360, 0, 0)],
    # "anubhav-cam-1": ["http://192.168.12.10:4747/video", (640, 360, 0, 0)],
    # "anubhav-cam-2": ["http://192.168.12.10:4747/video", (640, 360, 0, 0)],
    # "anubhav-cam-3": ["http://192.168.12.10:4747/video", (640, 360, 0, 0)],
    # "anubhav-cam-4": ["http://192.168.12.10:4747/video", (640, 360, 0, 0)],
    # "anubhav-cam-5": ["http://192.168.12.10:4747/video", (640, 360, 0, 0)],
    # "anubhav-cam-6": ["http://192.168.12.10:4747/video", (640, 360, 0, 0)],
    # "anubhav-cam-7": ["http://192.168.12.10:4747/video", (640, 360, 0, 0)],
    # "prakhar-cam-1": ["http://192.168.15.28:4747/video", (640, 360, 0, 0)],
    # "prakhar-cam-2": ["http://192.168.15.28:4747/video", (640, 360, 0, 0)],
    # "prakhar-cam-3": ["http://192.168.15.28:4747/video", (640, 360, 0, 0)],
    # "prakhar-cam-4": ["http://192.168.15.28:4747/video", (640, 360, 0, 0)],
    # "prakhar-cam-5": ["http://192.168.15.28:4747/video", (640, 360, 0, 0)],
    # "prakhar-cam-6": ["http://192.168.15.28:4747/video", (640, 360, 0, 0)],
    # "shivendra-webcam": ["http://192.168.12.11:5000", (640, 360, 0, 0)]
    # "vaibhav-cam-1": ["http://192.168.15.56:4747/video", (640, 360, 0, 0)],
    # "vaibhav-cam-2": ["http://192.168.15.56:4747/video", (640, 360, 0, 0)],
    # "vaibhav-cam-3": ["http://192.168.15.56:4747/video", (640, 360, 0, 0)],
    # "vaibhav-cam-4": ["http://192.168.15.56:4747/video", (640, 360, 0, 0)],
    # "vaibhav-cam-5": ["http://192.168.15.56:4747/video", (640, 360, 0, 0)],
    # "vaibhav-cam-6": ["http://192.168.15.56:4747/video", (640, 360, 0, 0)]
    "kshitij-cam": ["http://192.168.29.197:4747/video", (640, 360, 0, 0)],
    "kshititj-cam-2": ["http://192.168.15.4:4747/video", (640, 360, 0, 0)],
    # "kshititj-cam-3": ["http://192.168.0.116:4747/video", (640, 360, 0, 0)],
    # "kshititj-cam-4": ["http://192.168.0.116:4747/video", (640, 360, 0, 0)],
    # "kshititj-cam-5": ["http://192.168.0.116:4747/video", (640, 360, 0, 0)],
    # "kshititj-cam-6": ["http://192.168.0.116:4747/video", (640, 360, 0, 0)],
    # "kshititj-cam-7": ["http://192.168.0.116:4747/video", (640, 360, 0, 0)],
    # "kshititj-cam-8": ["http://192.168.0.116:4747/video", (640, 360, 0, 0)],
    # "riya-cam-2": ["http://192.168.17.91:4747/video", (640, 360, 0, 0)]
    # "kshitij-webcam": ["http://192.168.18.222:5000", (640, 360, 0, 0)],
}

# Set wait duration for IP cam re initialization if we are not able to initialize the cam
IP_CAM_REINIT_WAIT_DURATION = 10  # seconds
########################################################################################################################


########################################################################################################################
# Parameters specific to InsightFace-REST face detection
########################################################################################################################
# InsightFace-REST host
INSIGHTFACE_HOST = "http://192.168.12.1"

# InsightFace-REST port
INSIGHTFACE_PORT = "6385"  # 6385 for DGX, 18081 for the local system
# INSIGHTFACE_PORT_2 = "6385"

# Threaded GPU Flag
THREAD_FLAG = True
# Multi-Process GPU Flag
MULTIPROCESSING_FLAG = False

# Number of threads to be used for face recognition
NUMBER_OF_THREADS = 4

# Number of processes to be used for face recognition
NUMBER_OF_PROCESSES = 2

# Threshold
FACE_MATCHING_TOLERANCE = 0.9

# Boolean flag to indicate whether to save the landmarks of the images while creating embeddings
SAVE_LANDMARKS = False
########################################################################################################################


########################################################################################################################
# Parameters specific to Milvus Vector Database
########################################################################################################################
# Milvus host
MILVUS_HOST = "192.168.12.1"

# Milvus port
MILVUS_PORT = "19530"
########################################################################################################################


########################################################################################################################
# Parameters specific to Database Server Which Connects to Database (REDIS)
########################################################################################################################
# DATABASE Host
DATABASE_HOST = "192.168.12.1"  # IP of the machine where the database is running

# DATABASE port
DATABASE_PORT = 20001
########################################################################################################################


########################################################################################################################
# Parameters specific to Redis Database
########################################################################################################################
# Redis Host
REDIS_HOST = "192.168.12.1"

# Redis port
REDIS_PORT = 6381

# If the person is recognized by the same camera within this time threshold, the entry will not be added to the database
SAME_CAM_TIME_ENTRY_THRESHOLD = 5 * 60  # 5 minutes
########################################################################################################################


########################################################################################################################
# Parameters specific to Feedback Server Which Connects to Feedback Message Publisher (CONFLUENT-KAFKA)
########################################################################################################################
# FEEDBACK Host
FEEDBACK_HOST = "192.168.12.1"  # IP of the machine where the database is running

# FEEDBACK port
FEEDBACK_PORT = 20012
########################################################################################################################


########################################################################################################################
# Parameters specific to Feedback given to the user
########################################################################################################################
# Boolean flag to indicate whether to save the recognition frames
SAVE_RECOGNITION_FRAMES = False

# Boolean flag to indicate whether to enable the feedback server
ENABLE_FEEDBACK_SERVER = True

# File path where the recognition frames will be saved
RECOGNITION_PATH = "Recognition_Frames"

# Time after which the status is reset
STATUS_THRESHOLD = 1 * 60  # 1 minutes

# Time for which the kafka messages will be retained
KAFKA_MESSAGE_RETENTION = 10 * 1000  # 10 seconds

# Kafka host
KAFKA_HOST = "192.168.12.1"
# Kafka port
KAFKA_PORT = "9092"
########################################################################################################################

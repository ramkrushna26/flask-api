
from flask import Flask
from flask_restful import Api, Resource, reqparse, abort
from flask_sqlalchemy import 

# GET - Requesting data from specified resource
# POST - Create a resource 
# PUT - Update a resource
# DELETE - Delete a resource

app = Flask(__name__)
api = Api(app)

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video is required", required=True)
video_put_args.add_argument("views", type=int, help="Views of the video")
video_put_args.add_argument("likes", type=int, help="Likes on the video")

videos = {}

def abort_if_video_not_exist(video_id):
	if video_id not in videos:
		abort(404, message="Video Id is not valid...")

def abort_if_video_exist(video_id):
	if video_id not in videos:
		abort(409, message="Video Id is already exist...")

# create resource
class Vidoes(Resource):
	def get(self, video_id):
		abort_if_video_not_exist(video_id)
		return videos[video_id]

	def put(self, video_id):
		abort_if_video_exist(video_id)
		args = video_put_args.parse_args()
		videos[video_id] = args
		return 	videos[video_id], 201

	def delete(self, video_id):
		abort_if_video_not_exist
		del videos[video_id]
		return "", 204


# Add resource to Api
api.add_resource(Vidoes, "/video/<int:video_id>")

if __name__ == "__main__":
	# debug=True - only in DEV environment 
	app.run(debug=True)
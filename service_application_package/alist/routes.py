from flask import render_template, request, Blueprint, jsonify

aList = Blueprint('aList', __name__)


@aList.route('/viewList', methods=['GET']) #viewing all contents of aList
def get_List():
	List = mongo.db.List
	items = []
	item = List.find()
	for j in item:
		j.pop('_id')
		items.append(j)
	return jsonify(items)	
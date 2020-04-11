######################################################################################
######## this step is for searching with Elasticsearch 
######## don't change anything without permission please.
######################################################################################

es = Elasticsearch("http://elasticsearch:9200")

# this is your route to get a result on json array
@pro.route('/searchingProduct', methods=['POST'])
@require_appkey
def index():
#this is your key sended 
	nameProduct = request.json['nameProduct']
	body = {
	"size": 10,
    "query": {
        "prefix": {
            "name_product.keyword": nameProduct,
            }
        },
        "_source": ["name_product"]
    }
	results = es.search(index = 'product_db.product', body = body)
	numberOfResults = results['_shards']['successful'] - 1

	return jsonify({
		'msg': results['hits']['hits']
		})

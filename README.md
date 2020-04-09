
# What is MongoDB ?
MongoDB is a document database with the scalability and stores data in flexible, JSON-like documents, meaning fields can vary from document to document and data structure can be changed over time.
# What is ElasticSearch ?
Elasticsearch is a search engine based on Lucene.It uses a document-oriented approach when manipulating data which is stored in JSON format.
# Sounds similar , what's the difference?
Elasticsearch is a highly scalable open source full-text search and analytics engine, whereas MongoDB is next-generation database.Unlike MongoDB, ElasticSearch is not yet ready for use as main storage for data.
Elasticsearch is generally used as the underlying engine/technology that powers applications that have complex search features and requirements. MongoDB is not a search engine but it has full text search feature.
# Who uses Elasticsearch?
eBay, Facebook, Uber, github, Microsoft, Just Eat.

# Sync mongodb to elasticsearch

<h6 color="red">Mongodb-River:</h6>
unfortunately this plugin is not supporting the latest version of Elasticsearch but only support 1.7- and you are not lucky to use real time sync .

<h6 color="red">Mongo-connector:</h6>
A decent python based library, but unfortunately haven’t been updated for almost a two year, not to mention that it does not support Elasticsearch version 6+ out of the box, only support Elasticsearch 5-.

Transporter:
A great and updated frequently library, but it does not actually sync the data between mongodb and Elasticsearch in real time! Which means that it’s job is done once the sync is done. 

# What is Monstache ?
Monstache is a sync daemon written in Go that continuously indexes your MongoDB collections into Elasticsearch. Monstache gives you the ability to use Elasticsearch to do complex searches and aggregations of your MongoDB data and easily build realtime Kibana visualizations and dashboards.
documentation for Monstache : https://rwynn.github.io/monstache-site/
github : https://github.com/rwynn/monstache


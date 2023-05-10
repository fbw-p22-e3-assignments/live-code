# APIs (Application Programming Interface)

**What is an API?**

***Application Programming Interface (API)*** is a software interface that allows two applications to interact with each other without any user intervention. API is a collection of software functions and procedures. In simple terms, API means a software code that can be accessed or executed. API is defined as a code that helps two different software’s to communicate and exchange data with each other.

**What is Web APIs?**

A Web API is an application programming interface which is use either for web server or a web browser. APIs come in many types and forms. Which one a developer chooses among a variety of API protocols and standards depends on the purpose. The common API types include:

**REST-based APIs:**
A data-driven architectural style of API development, REST (Representational State Transfer) is one of the most lucrative categories of web-based APIs. Based on Uniform Resource Identifiers (URIs) and HTTP protocol, REST-based APIs use JSON for data formatting which is considered to be browser-compatible.

REST-based APIs are extremely simple when it comes to building and scaling as compared to other types of APIs. When these types of APIs are put to action, they help facilitate client-server communications with ease and smoothness. Because REST-based APIs are simple, they can be the perfect APIs for beginners.

**SOAP-based APIs:**
As compared to its peers, SOAP-based APIs (Simple Object Access Protocol) can be viewed as quite complex in terms of use. These APIs use a type of protocol known as Simple Object Access Protocol, which is a common communication protocol. This helps them in providing higher levels of security and makes them better at accuracy as compared with the REST-based APIs in the way messages are exchanged.

**GraphQL-based APIs:**
GraphQL is one of the most advanced sets of web-based APIs where open-source data query and manipulation language is used. This makes it easier for forming a definitive pathway for the runtime that plays a vital role in fulfilling queries with the pre-existing data.

Although it is well known that GraphQL and REST APIs both use the same set of APIs, the major thing that differentiates them is the interface: a single interface-id is put to use by GraphQL when it comes to organizing data into the format of a graph.

**XML-RPC:**
XML-RPC (Extensible Markup Language-Remote Procedure Call) can be described as another type of API protocol, which differentiates itself in terms of information security and the use of XML format that is specifically designed for transferring data. When compared to SOAP-based APIs, the XML-RPC protocols are easier and much simpler to use since they use minimum bandwidth.

Examples of web API:

* Google Maps API’s allow developers to embed Google Maps on webpages by using a JavaScript or Flash interface.
* YouTube API allows developers to integrate YouTube videos and functionality into websites or applications.
* Twitter offers two APIs. The REST API helps developers to access Twitter data, and the search API provides methods for developers to interact with Twitter Search.
* Amazon’s API gives developers access to Amazon’s product selection.

**What is REST?**

REST is an architecture consisting of best practices and patterns for web development. It is a set of guidelines for developers rather than a true protocol. Websites and applications are considered RESTful if they follow REST principles. REST is now the industry-standard model for client-server interactions on the web, and most popular web services are only accessible through REST interfaces. The most important REST guidelines are as follows:

* **Client-server Architecture:** Clients and servers are loosely coupled and communicate via an API.
* **Statelessness:** Requests are independent and do not rely on the current state of the transaction.
* **Caches:** Caches are used for better performance and increased security.
* **Layering:** Additional features, such as security protocols, can be added to REST as a separate layer. For example, the user can be authenticated and then the request can be passed to another layer for processing.
* **Uniform interfaces:** Clients use well-known ***Uniform Resource Indicator (URIs)*** to request information. They must identify the specific resource to access and the format to use. The services are not customizable, so clients must use the official generic interface.

REST principles are straightforward. Clients use a Uniform Resource Identifier (URI) to request information from a server. Inside the message, which is typically sent using HTTP, the client identifies the resources it wants. It can also specify a format for the reply. The server replies with the requested data, in ***JavaScript Object Notation (JSON)***, HTML, or XML. A REST request includes the following components:

* An HTTP method indicating the requested operation, such as `GET` or `PUT`.
* A header, including the media type the sender wants to receive. Some examples are `text/css` and `image/gif`.
* The URI to the resource, including any optional parameters. A client can specify the URI using the formats `example.com/products/137` or `example.com/products/:id`.

The REST architecture is an industry standard because it offers many advantages. Some of its advantages are as follows:

* It is scalable, fast, robust, and efficient. REST APIs do not use much bandwidth.
* It is easy to understand and implement.
* It promotes modular architecture and good design.
* Clients and servers are fully decoupled. It is easier to make changes to the API or the internal design and is more secure.
* It allows many different message formats.

However, REST cannot process any requests based on the state of the transaction. It also does not guarantee reliability or include any security features. Client applications must implement these features.

**What are RESTful Verbs?**

REST interfaces allow for a fixed set of interactions. Taken together, these operations are known as the *RESTful verbs* or *REST verbs.* Each RESTful verb indicates an action on the client-side application.

Each distinct operation is associated with a specific RESTFul verb and a range of possible status codes. A client like postman or curl must include a RESTful verb inside the HTTP header for each request. The RESTful verbs correspond to the main create, read, update, and delete (CRUD) database operations.

Here are the main RESTful verbs that allow clients to use a REST API:

* **POST**: This RESTful verb creates a new resource on the server. If successful, the `POST` action returns code `201` for “Created” and provides a link to the new reference. Failure codes include `404` for “Not Found”, or a `409` conflict error if the item already exists.
* **GET**: `GET` is used to retrieve information from the server. It can read an entire list or one specific item, and returns code `200` for “OK” if successful. If the item or collection cannot be found, the server returns code `404`.
* **PUT**: The `PUT` REST verb is used to update a specific item. The client must specify all attributes for the item. This method returns the status code `200` when the item is updated. The server returns either `404` for “Not Found” or `405` for “Method Not Allowed” if the update fails.
* **PATCH**: This REST verb is similar to `PUT`. It modifies the item, but only contains the new changes, not the entire item. However, this verb is not considered safe from collisions. It is not recommended and is not used very much.
* **DELETE**: The `DELETE` RESTful verb deletes an entry from the database, although it can also potentially delete the entire collection. It returns code `200` when successful, and code `404` or `405` otherwise.
* **OPTIONS**: This verb fetches a list of all available operations.

For almost all APIs, the `POST`, `PUT`, `PATCH`, and `DELETE` operations require server authentication. However, many servers allow anonymous `GET` operations for public data. If the server cannot authorize a user, it returns the failure code `401` for “Unauthorized”. Failure code `403`, or “Forbidden”, is used if the client is not allowed to access the resource.

## Testing APIs using Postman Client

**What is Postman?**

Postman is an API testing tool that allows you to perform comprehensive testing faster. It offers:

* a simple user interface where each integral part of the API lifecycle can be easily visualized and understood.
* pre-built code snippets that can be used for verifying tests or for generating test data used in tests.
* a wide range of options, for example, testing on different environments, testing on different servers, documentation of the API, collaboration and sharing the API with teammates or with the world.

**Postman Workspaces**

A Postman workspace is where you can organize your API and team up with others in your organization.

There are three kinds of workspaces in Postman:

1. Personal workspace, as the name suggests, is for personal usage.
2. Private workspace is only available to people who you invite to collaborate within the workspace. Then, you can organize it into folders and share it with your workspace members.
3. Public Workspaces allow you to share your APIs with the world. They are searchable and accessible for free.

Postman’s API testing features are available for Personal, Private, and Public workspaces.

**Creating a new workspace**
To create a new workspace, select Workspaces in the header, then select Create Workspace.

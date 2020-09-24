Application Structure
---------------------
├── app.py              ~ Main application to start with
├── data_files          ~ Contains the simple version of json files acting as data storage
│   ├── gift_links.json ~ Contains the data related to the wedding gifts link creted by the users
│   ├── products.json   ~ Original copy of the supplied products list
│   └── user_auth.json  ~ Used for user authentication (very basic)
├── data.py             ~ Contains all the data related functions
├── static
│   ├── css
│   │   └── index.css
│   └── img
│       └── img.png
└── templates
    ├── create_link.html ~ User can use this page for creating new a link for wedding gifts
    ├── edit_list.html   ~ Used to edit the gift list items (add / delete)
    ├── gift_link.html   ~ View the list items along with report of purchased items from the selected list
    ├── home.html        ~ Dashboard / Home page of the user
    ├── includes
    │   └── _navbar.html ~ Nav bar snippet html file
    ├── index.html       ~ Landing page of the application containing Login details
    └── _main.html       ~ Basic layout html file included in all other html files

Recomendations ( can implement if more time permits)
---------------
1. Can improve the application look and feel by adding more styling components
2. Instead of using JSON files as storage can go for a database providing more security
3. This application can also be designed more with Javascript or Jquery using Flask as the backbone for data API's

var api = new RestClient('http://localhost:5000');

api.res("xd");

api.xd.get().then(function(e) {
    console.log(e);
});
$.mockjax({
  url: '/api/members/check',
  
  responseTime: 100,
  status: 200,
  response: function(settings) {
  	if (settings.data.username == "Ahmed") {
  		this.responseText = true;
  	} else {
  		this.contentType = "application/json";
  	}
  	  	
  },
});

var Utils = (function() {
	var clearIndicator = function(element) {
		$(element).removeClass("inactive active correct not-correct").addClass('hidden');
	};

	var correctIndicator = function(element) {
		clearIndicator(element);
		$(element).addClass('active correct').removeClass('hidden');
	};

	var incorrectIndicator = function(element) {
		clearIndicator(element);
		$(element).addClass('inactive not-correct').removeClass('hidden');
	};
	
	var showAlert = function(message, alertType) {
		var element = "#form-alert";
	    var alertElem = $('<div class="alert-message ' + alertType + ' fade in" data-alert="alert">' +
    	  '<a class="close" href="#">×</a>' + 
    	  '<p>' + message + '</p></div>').hide();
    	 $.scrollTo(element, 500);
    	 $(element).append(alertElem);
    	 alertElem.fadeIn();
    	 
	}
	var resetForm = function(element) {
		$(element).resetForm();
		$("#newMember label[id$='-indicator']").each(function(index) {
			Utils.clearIndicator($(this));
		});
		$('#photoPreview img').remove();
 		$('.qq-upload-list li').remove();
	}
	return {
		clearIndicator: clearIndicator,
		correctIndicator: correctIndicator,
		incorrectIndicator: incorrectIndicator,
		showAlert: showAlert,
		resetForm: resetForm
		}
})();

var Member = (function() {	
	var removeById = function(memberId) {
		console.log("Member Deleted");
	};

	var remove = function(memberId) {
		console.log("Member Deleted");
	};
	
	var update = function(member) {
		console.log("Member updated");
	}
	var showPreview = function(id, fileName, responseJSON) {
		if (responseJSON.success == true) {
			var elem = $('<img src="/api/tmp_photo?filename=' + responseJSON.filename + '" />');
			$('#photoPreview').html(elem);
			$('#newMember input[name=photo]').attr("value", responseJSON.filename);
		} else {
			Utils.showAlert("Server rejected the uploaded photo, the reason is '"+ responseJSON.reason +"'", "error");
		}
	}
	var checkField = function(field, value, onAvailable, onNotAvailable) {
		$.ajax({
			url: "/api/is_available",
			data: {field: field,
				   value: value},
			success: function(data) {
				if (data == true) {
					onAvailable();
				} else {
					onNotAvailable();
				}
			}		
		});		
		
	};
	return {
		update: update,
		remove: remove,
		removeById: removeById,
		checkField: checkField,
		showPreview: showPreview
	}
})();


// Initialization
var initFormTriggers = function() {
	var checkFieldOnInput = function(selector, fieldName, indicatorSelector) {
		$(selector).blur(function() {
			var value = this.value;
			if (value.length == 0) {
				return;
			}
			Member.checkField(fieldName, value, function(){
				Utils.correctIndicator(indicatorSelector);
			}, function() {
				Utils.incorrectIndicator(indicatorSelector);
			});
		});		
	}
	

 	// fields
 	checkFieldOnInput('#username', 'username', '#username-indicator');
	checkFieldOnInput('#email', 'email', '#email-indicator');
	checkFieldOnInput('#national-id', 'national_id', '#national-id-indicator');
	checkFieldOnInput('#twitter', 'twitter_id', '#twitter-indicator');
	
	var uploader = new qq.FileUploader({
		//TODO: remember to check for max size
    element: $('#file-uploader')[0],
    // path to server-side upload script
    action: '/api/photo_upload',
    allowedExtensions: ['png', 'jpg', 'bmp', 'gif'],
    multiple: false,
    sizeLimit: 1024 * 1024,
    onComplete: Member.showPreview
    
});
} // end of initialization function




$(document).ready(function() {
	// form trigger
	$('#newMember').ajaxForm({ success: function (response, statusTxt) {
	        if (response.success == true) {
				Utils.showAlert("New member (<strong>" + $('#newMember input[name=username]')[0].value + "</strong>) is added with id (<strong>" + response.member_id +"</strong>)", "success");
				Utils.resetForm('#newMember');
	        } else {
	        	console.log(response);
	        	Utils.showAlert("Couldn't add new member because: (" + response.reason +")", "error");
	        }	
		},
		error: function(response) {
			Utils.showAlert("ERROR: Cannot add new member because (" + response +")", "error");
			console.log(response);
		},
		dataType: "json"
		
	});

	initFormTriggers();
});




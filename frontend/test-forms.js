Survey.StylesManager
    .applyTheme("bootstrap");

// Survey.Serializer.addProperty("page", {
//         name: "navigationTitle:string",
//         isLocalizable: true
//     });
// Survey.Serializer.addProperty("page", {
//         name: "navigationDescription:string",
//         isLocalizable: true
//     });

var surveyJSON = {
	"pages":[
	{
		"name":"page1",
		"elements":[
		{
			"type":"dropdown",
			"name":"question1",
			"title":"How old are you?",
			"isRequired":true,
			"requiredErrorText":
			"Please select an option to proceed.",
			"choices":[
			{
				"value":"item1","text":"Under 18"},
				{"value":"item2","text":"18-24"},
				{"value":"item3","text":"25-34"},
				{"value":"item4","text":"35-44"},
				{"value":"item5","text":"45-54"},
				{"value":"item6","text":"55-64"},
				{"value":"item7","text":"65+"}],
				"otherText":"45-54"
		},
		{
			"type":"radiogroup",
			"name":"question2",
			"title":"What is your gender?",
			"isRequired":true,
			"requiredErrorText":"Please select an option to proceed.",
			"choices":[
			{
				"value":"item1","text":"Female"},
				{"value":"item2","text":"Male"},
				{"value":"item3","text":"Transgender"}],
				"hasOther":true,
				"otherText":"Prefer not to say"
		},
		{
			"type":"radiogroup",
			"name":"question3",
			"title":"What is your sexual orientation?",
			"isRequired":true,
			"requiredErrorText":"Please select an option to proceed.",
			"choices":[
			{
				"value":"item1","text":"Heterosexual"},
				{"value":"item2","text":"Homosexual"},
				{"value":"item3","text":"Bisexual"},
				{"value":"item4","text":"Pansexual"},
				{"value":"item5","text":"Asexual"}]}]
		},
		{
			"name":"page2","elements":[{"type":"rating","name":"question5","title":"Please rate yourself on each of the following values:","description":"Education/Knowledge/Street Smarts","rateValues":[{"value":1,"text":"0 - I suck"},{"value":2,"text":"1"},{"value":3,"text":"2"},{"value":4,"text":"3"},{"value":5,"text":"4"},{"value":6,"text":"5 - I am decent"},{"value":7,"text":"6"},{"value":8,"text":"7"},{"value":9,"text":"8"},{"value":10,"text":"9"},{"value":"11","text":"10 - I am excellent"}],"rateMax":10},{"type":"rating","name":"question6","title":"Please rate yourself on each of the following values:","description":"Financial Choices","rateValues":[{"value":1,"text":"0 - I suck"},{"value":2,"text":"1"},{"value":3,"text":"2"},{"value":4,"text":"3"},{"value":5,"text":"4"},{"value":6,"text":"5 - I am decent"},{"value":7,"text":"6"},{"value":8,"text":"7"},{"value":9,"text":"8"},{"value":10,"text":"9"},{"value":"11","text":"10 - I am excellent"}],"rateMax":10},{"type":"rating","name":"question7","title":"Please rate yourself on each of the following values:","description":"Confidence/Self-Esteem","rateValues":[{"value":1,"text":"0 - I suck"},{"value":2,"text":"1"},{"value":3,"text":"2"},{"value":4,"text":"3"},{"value":5,"text":"4"},{"value":6,"text":"5 - I am decent"},{"value":7,"text":"6"},{"value":8,"text":"7"},{"value":9,"text":"8"},{"value":10,"text":"9"},{"value":"11","text":"10 - I am excellent"}],"rateMax":10},{"type":"rating","name":"question8","title":"Please rate yourself on each of the following values:","description":"Religious/Spiritual Values","rateValues":[{"value":1,"text":"0 - I suck"},{"value":2,"text":"1"},{"value":3,"text":"2"},{"value":4,"text":"3"},{"value":5,"text":"4"},{"value":6,"text":"5 - I am decent"},{"value":7,"text":"6"},{"value":8,"text":"7"},{"value":9,"text":"8"},{"value":10,"text":"9"},{"value":"11","text":"10 - I am excellent"}],"rateMax":10},{"type":"rating","name":"question9","title":"Please rate yourself on each of the following values:","description":"Materialism/Superficiality","rateValues":[{"value":1,"text":"0 - I suck"},{"value":2,"text":"1"},{"value":3,"text":"2"},{"value":4,"text":"3"},{"value":5,"text":"4"},{"value":6,"text":"5 - I am decent"},{"value":7,"text":"6"},{"value":8,"text":"7"},{"value":9,"text":"8"},{"value":10,"text":"9"},{"value":"11","text":"10 - I am excellent"}],"rateMax":10},{"type":"rating","name":"question10","title":"Please rate yourself on each of the following values:","description":"Image/Fashion Sense/Body Modification","rateValues":[{"value":1,"text":"0 - I suck"},{"value":2,"text":"1"},{"value":3,"text":"2"},{"value":4,"text":"3"},{"value":5,"text":"4"},{"value":6,"text":"5 - I am decent"},{"value":7,"text":"6"},{"value":8,"text":"7"},{"value":9,"text":"8"},{"value":10,"text":"9"},{"value":"11","text":"10 - I am excellent"}],"rateMax":10},{"type":"rating","name":"question11","title":"Please rate yourself on each of the following values:","description":"Occupation/Work Ethic/Self-Discipline","rateValues":[{"value":1,"text":"0 - I suck"},{"value":2,"text":"1"},{"value":3,"text":"2"},{"value":4,"text":"3"},{"value":5,"text":"4"},{"value":6,"text":"5 - I am decent"},{"value":7,"text":"6"},{"value":8,"text":"7"},{"value":9,"text":"8"},{"value":10,"text":"9"},{"value":"11","text":"10 - I am excellent"}],"rateMax":10},{"type":"rating","name":"question12","title":"Please rate yourself on each of the following values:","description":"Household Care, Maintenance and Cleanliness","rateValues":[{"value":1,"text":"0 - I suck"},{"value":2,"text":"1"},{"value":3,"text":"2"},{"value":4,"text":"3"},{"value":5,"text":"4"},{"value":6,"text":"5 - I am decent"},{"value":7,"text":"6"},{"value":8,"text":"7"},{"value":9,"text":"8"},{"value":10,"text":"9"},{"value":"11","text":"10 - I am excellent"}],"rateMax":10},{"type":"rating","name":"question13","title":"Please rate yourself on each of the following values:","description":"Communication Style/Manners","rateValues":[{"value":1,"text":"0 - I suck"},{"value":2,"text":"1"},{"value":3,"text":"2"},{"value":4,"text":"3"},{"value":5,"text":"4"},{"value":6,"text":"5 - I am decent"},{"value":7,"text":"6"},{"value":8,"text":"7"},{"value":9,"text":"8"},{"value":10,"text":"9"},{"value":"11","text":"10 - I am excellent"}],"rateMax":10},{"type":"rating","name":"question14","title":"Please rate yourself on each of the following values:","description":"Artsy/Creative/Musical","rateValues":[{"value":1,"text":"0 - I suck"},{"value":2,"text":"1"},{"value":3,"text":"2"},{"value":4,"text":"3"},{"value":5,"text":"4"},{"value":6,"text":"5 - I am decent"},{"value":7,"text":"6"},{"value":8,"text":"7"},{"value":9,"text":"8"},{"value":10,"text":"9"},{"value":"11","text":"10 - I am excellent"}],"rateMax":10},{"type":"rating","name":"question15","title":"Please rate yourself on each of the following values:","description":"Charitable/Philanthropic","rateValues":[{"value":1,"text":"0 - I suck"},{"value":2,"text":"1"},{"value":3,"text":"2"},{"value":4,"text":"3"},{"value":5,"text":"4"},{"value":6,"text":"5 - I am decent"},{"value":7,"text":"6"},{"value":8,"text":"7"},{"value":9,"text":"8"},{"value":10,"text":"9"},{"value":"11","text":"10 - I am excellent"}],"rateMax":10},{"type":"rating","name":"question16","title":"Please rate yourself on each of the following values:","description":"Pursuing a Greater Purpose","rateValues":[{"value":1,"text":"0 - I suck"},{"value":2,"text":"1"},{"value":3,"text":"2"},{"value":4,"text":"3"},{"value":5,"text":"4"},{"value":6,"text":"5 - I am decent"},{"value":7,"text":"6"},{"value":8,"text":"7"},{"value":9,"text":"8"},{"value":10,"text":"9"},{"value":"11","text":"10 - I am excellent"}],"rateMax":10},{"type":"rating","name":"question17","title":"Please rate yourself on each of the following values:","description":"Social Status/Sociability","rateValues":[{"value":1,"text":"0 - I suck"},{"value":2,"text":"1"},{"value":3,"text":"2"},{"value":4,"text":"3"},{"value":5,"text":"4"},{"value":6,"text":"5 - I am decent"},{"value":7,"text":"6"},{"value":8,"text":"7"},{"value":9,"text":"8"},{"value":10,"text":"9"},{"value":"11","text":"10 - I am excellent"}],"rateMax":10},{"type":"rating","name":"question18","title":"Please rate yourself on each of the following values:","description":"Cultured/Well-traveled/\"Woke\"","rateValues":[{"value":1,"text":"0 - I suck"},{"value":2,"text":"1"},{"value":3,"text":"2"},{"value":4,"text":"3"},{"value":5,"text":"4"},{"value":6,"text":"5 - I am decent"},{"value":7,"text":"6"},{"value":8,"text":"7"},{"value":9,"text":"8"},{"value":10,"text":"9"},{"value":"11","text":"10 - I am excellent"}],"rateMax":10},{"type":"rating","name":"question19","title":"Please rate yourself on each of the following values:","description":"Self-Care/Personal Hygiene/Cleanliness","rateValues":[{"value":1,"text":"0 - I suck"},{"value":2,"text":"1"},{"value":3,"text":"2"},{"value":4,"text":"3"},{"value":5,"text":"4"},{"value":6,"text":"5 - I am decent"},{"value":7,"text":"6"},{"value":8,"text":"7"},{"value":9,"text":"8"},{"value":10,"text":"9"},{"value":"11","text":"10 - I am excellent"}],"rateMax":10},{"type":"rating","name":"question20","title":"Please rate yourself on each of the following values:","description":"Honesty/Dependable/Reliable","rateValues":[{"value":1,"text":"0 - I suck"},{"value":2,"text":"1"},{"value":3,"text":"2"},{"value":4,"text":"3"},{"value":5,"text":"4"},{"value":6,"text":"5 - I am decent"},{"value":7,"text":"6"},{"value":8,"text":"7"},{"value":9,"text":"8"},{"value":10,"text":"9"},{"value":"11","text":"10 - I am excellent"}],"rateMax":10},{"type":"rating","name":"question21","title":"Please rate yourself on each of the following values:","description":"Family Values","rateValues":[{"value":1,"text":"0 - I suck"},{"value":2,"text":"1"},{"value":3,"text":"2"},{"value":4,"text":"3"},{"value":5,"text":"4"},{"value":6,"text":"5 - I am decent"},{"value":7,"text":"6"},{"value":8,"text":"7"},{"value":9,"text":"8"},{"value":10,"text":"9"},{"value":"11","text":"10 - I am excellent"}],"rateMax":10},{"type":"dropdown","name":"question4","title":"Please choose the top 5 values you seek in a partner.","isRequired":true,"choices":[{"value":"item1","text":"Education/Knowledge/Street Smarts"},{"value":"item2","text":"Financial Choices"},{"value":"item3","text":"Confidence/Self-Esteem"},{"value":"item4","text":"Religious/Spiritual Values"},{"value":"item5","text":"Materialism/Superficiality"},{"value":"item6","text":"Image/Fashion Sense/Body Modification"},{"value":"item7","text":"Occupation/Work Ethic/Self-Discipline"},{"value":"item8","text":"Household Care, Maintenance and Cleanliness"},{"value":"item9","text":"Communication Style/Manners"},{"value":"item10","text":"Artsy/Creative/Musical"},{"value":"item11","text":"Charitable/Philanthropic"},{"value":"item12","text":"Pursuing a Greater Purpose"},{"value":"item13","text":"Social Status/Sociability"},{"value":"item14","text":"Cultured/Well-traveled/\"Woke\""},{"value":"item15","text":"Self-Care/Personal Hygiene/Cleanliness"},{"value":"item16","text":"Honesty/Dependable/Reliable"}],"otherText":"Family Values","choicesMin":5,"choicesMax":5}],"title":"Relationship Values/Types","description":"This series of questions will identify a list of values and traits for you to consider. You will be asked to rate yourself for each of these values/traits, as well as to identify the top 5 values/traits you seek in a romantic partner."}]}

window.survey = new Survey.Model(surveyJSON);

survey.onComplete.add(function (result) {
	document.querySelector('#surveyResult')
	.textContent = "Result JSON:\n" + JSON.stringify(result.data, null, 3);
});

$("#surveyElement").Survey({model: survey});


var navTopEl = document.querySelector("#surveyNavigationTop");
navTopEl.className = "navigationContainer";
var navProgBarDiv = document.createElement("div");
navProgBarDiv.className = "navigationProgressbarDiv";
navTopEl.appendChild(navProgBarDiv);
var navProgBar = document.createElement("ul");
navProgBar.className = "navigationProgressbar";
navProgBarDiv.appendChild(navProgBar);


var liEls = [];
for (var i = 0; i < survey.visiblePageCount; i++) {
	var liEl = document.createElement("li");
	if (survey.currentPageNo == i) {
		liEl.classList.add("current");
	}
	liEl.onclick = function (index) {
		return function() {
			if (survey['isCompleted'])
				return;
			liEl
			s[survey.currentPageNo]
				.classList.remove("current");
			if (index < survey.currentPageNo) {
				survery.currentPageNo = index;
			} else if (index > survey.currentPageNo) {
				var j = survey.currentPageNo;
				for (; j < index; j++) {
					if (survey.visiblePages[j].hasErrors(true, true))
						break;
					if (!liEls[j].classList.contains("completed")) {
						liEls[j].classList.add("completed");
					}
				}
				survey.currentPageNo = j;
			}
			liEls[survey.currentPageNo]
				.classList.add("current");
		};
	}(i);
	var pageTitle = document.createElement("span");
	if (!survey.visiblePages[i].navigationTitle) {
		pageTitle.innerText = survey
			.visiblePages[i]
			.name;
	} else
		pageTitle.innerText = survey
			.visiblePages[i]
			.navigationTitle;
	pageTitle.className = "pageTitle";
	liEl.appendChild(pageTitle);
	var br = document.createElement("br");
	liEl.appendChild(br);
	var pageDescription = document.createElement("span");
	if (!!survey.visiblePages[i].navigationDescription) {
		pageDescription.innerText = survey
			.visiblePages[i]
			.navigationDescription;
	}
	pageDescription.className = "pageDescription";
	liEl.appendChild(pageDescription);
	liEls.push(liEl);
	navProgBar.appendChild(liEl);
}
survey.onCurrentPageChanged
	.add(function (sender, options) {
		var oldIndex = options.oldCurrentPage.visibleIndex;
		var newIndex = options.newCurrentPage.visibleIndex;
		liEls[oldIndex]
			.classList
			.remove("current");
		if (newIndex > oldIndex) {
			for (var i = oldIndex; i < newIndex; i++) {
				if (sender.visiblePages[i].hasErrors(true, true))
					break;
				if (!liEls[i].classList.contains("completed")) {
					liEls[i]
						.classList
						.add("completed");
				}
			}
		}
		liEls[newIndex]
			.classList
			.add("current");
	});

survey
    .onComplete
    .add(function (sender, options) {
        liEls[sender.currentPageNo]
            .classList
            .remove("current");
        for (var i = 0; i < sender.visiblePageCount; i++) {
            if (survey.visiblePages[i].hasErrors(true, true)) 
                break;
            if (!liEls[i].classList.contains("completed")) {
                liEls[i]
                    .classList
                    .add("completed");
            }
        }
    });

// var updateScroller = setInterval(() => {
//     if (navProgBarDiv.scrollWidth <= navProgBarDiv.offsetWidth) {
//         leftImg
//             .classList
//             .add("hidden");
//         rightImg
//             .classList
//             .add("hidden");
//     } else {
//         leftImg
//             .classList
//             .remove("hidden");
//         rightImg
//             .classList
//             .remove("hidden");
//     }
// }, 100);




// function sendDataToServer(survey) {
//     //send Ajax request to your web server.
//     alert("The results are:" + JSON.stringify(survey.data));
// }

// var survey = new Survey.Survey(surveyJSON);
// $("#surveyContainer").Survey({
//     model: survey,
//     onComplete: sendDataToServer
// });
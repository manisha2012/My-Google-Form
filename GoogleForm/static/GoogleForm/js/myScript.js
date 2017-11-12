var myScript = (function () {

    var _defaults = {
        questionTypeMenuArray : ['Dropdown', 'Checkboxes', 'Multiple Choice']
    };

    el = {
        shortTypeQues : myDom.getElById('short'),
        singleTypeQues : myDom.getElById('single'),
        multipleTypeQues : myDom.getElById('multiple'),
        quesCount : myDom.getElById('quesCount').val(),
        formContainer : myDom.getElById('formContainer')
    };

    methods = {

        _getShortQuestionOptionMarkup : function (event) {
            el.quesCount++;
            myDom.getElById('quesCount').val(el.quesCount);
            var shortQuesMarkup = $('<div class="row">' +
                    '<div class="col-sm-12">' +
                        '<div class="row">' +
                            '<div class="col-sm-12 questionTitle">' +
                                '<div class="mdl-textfield mdl-js-textfield">' +
                                    '<input class="mdl-textfield__input" type="text" id="short-ques_'+el.quesCount+'" name="ques_title'+el.quesCount+'">' +
                                    '<label class="mdl-textfield__label" for="short-ques_'+el.quesCount+'">Give title to your question...</label>' +
                                '</div>' +
                            '</div>' +
                        '</div>' +
                        '<div class="row">' +
                            '<div class="col-sm-12 questionTitle">' +
                                '<div class="mdl-textfield mdl-js-textfield">' +
                                    '<input class="mdl-textfield__input" type="hidden" name="ques_type'+el.quesCount+'" value="SH">' +
                               '</div>' +
                            '</div>' +
                        '</div>' +
                        '<div class="row">' +
                            '<div class="col-sm-12">' +
                                '<div class="mdl-textfield mdl-js-textfield">' +
                                    '<input class="mdl-textfield__input" type="text" disabled>' +
                                    '<label class="mdl-textfield__label">Write answer here..</label>' +
                                '</div>' +
                            '</div>' +
                        '</div>' +
                     '</div>' +
                '</div>');
            el.formContainer.append(shortQuesMarkup);
        },
        _getSingleQuestionOptionMarkup : function (event) {
            el.quesCount++;
            myDom.getElById('quesCount').val(el.quesCount);
            var singleQuesMarkup = $('<div class="row">' +
                    '<div class="col-sm-12">' +
                        '<div class="row">' +
                            '<div class="col-sm-12 questionTitle">' +
                                '<div class="mdl-textfield mdl-js-textfield">' +
                                    '<input class="mdl-textfield__input" type="text" name="ques_title'+el.quesCount+'">' +
                                    '<label class="mdl-textfield__label" >Give title to your question...</label>' +
                               '</div>' +
                            '</div>' +
                        '</div>' +
                        '<div class="row">' +
                            '<div class="col-sm-12 questionTitle">' +
                                '<div class="mdl-textfield mdl-js-textfield">' +
                                    '<input class="mdl-textfield__input" type="hidden" name="ques_type'+el.quesCount+'" value="SC">' +
                               '</div>' +
                            '</div>' +
                        '</div>' +
                        '<div class="row">' +
                            '<div class="col-sm-1 optionBox"><span class="glyphicon glyphicon-unchecked"></span></div>' +
                            '<div class="col-sm-11">'+
                                '<div class="mdl-textfield mdl-js-textfield">'+
                                    '<input class="mdl-textfield__input" type="text" name="option_single_'+el.quesCount+'_1">'+
                                    '<label class="mdl-textfield__label">Option 1</label>'+
                                '</div>'+
                            '</div>'+
                            '<div class="col-sm-1 optionBox"><span class="glyphicon glyphicon-unchecked"></span></div> '+
                            '<div class="col-sm-11">'+
                                '<div class="mdl-textfield mdl-js-textfield">'+
                                    '<input class="mdl-textfield__input" type="text" name="option_single_'+el.quesCount+'_2">'+
                                    '<label class="mdl-textfield__label">Option 2</label>'+
                                '</div>'+
                            '</div>'+
                        '</div>'+

                     '</div>'+
               '</div>');
            el.formContainer.append(singleQuesMarkup);
        },
        _getMultipleQuestionOptionMarkup : function (event) {
            el.quesCount++;
            myDom.getElById('quesCount').val(el.quesCount);
            var multipleChoice = $('<div class="row">'+
                    '<div class="col-sm-12 questionBlock">'+
                        '<div class="row">'+
                            '<div class="col-sm-12 questionTitle">'+
                                '<div class="col-sm-9 questionTitle">'+
                                    '<div class="mdl-textfield mdl-js-textfield">'+
                                        '<input class="mdl-textfield__input" type="text" id="ques3" name="ques_title'+el.quesCount+'">'+
                                        '<label class="mdl-textfield__label" for="ques3">Give title to your question...</label>'+
                                    '</div>'+
                                '</div>'+
                            '</div>'+
                        '</div>'+
                        '<div class="row">' +
                            '<div class="col-sm-12 questionTitle">' +
                                '<div class="mdl-textfield mdl-js-textfield">' +
                                    '<input class="mdl-textfield__input" type="hidden" name="ques_type'+el.quesCount+'" value="MC">' +
                               '</div>' +
                            '</div>' +
                        '</div>' +
                        '<div class="row">'+
                            '<div class="col-sm-1 optionBox"><span class="glyphicon glyphicon-record"></span></div> '+
                            '<div class="col-sm-11">'+
                                '<div class="mdl-textfield mdl-js-textfield">'+
                                    '<input class="mdl-textfield__input" type="text" id="multiple-choice-1" name="option_mul_'+el.quesCount+'_1">'+
                                    '<label class="mdl-textfield__label" for="multiple-choice-1">Option 1</label>'+
                                '</div>'+
                            '</div>'+
                            '<div class="col-sm-1 optionBox"><span class="glyphicon glyphicon-record"></span></div> '+
                            '<div class="col-sm-11">'+
                                '<div class="mdl-textfield mdl-js-textfield">'+
                                    '<input class="mdl-textfield__input" type="text" id="multiple-choice-2" name="option_mul_'+el.quesCount+'_2">'+
                                    '<label class="mdl-textfield__label" for="multiple-choice-2">Option 2</label>'+
                                '</div>'+
                            '</div>'+
                        '</div>'+

                        '<div class="row">'+
                            '<div class="col-sm-1 optionBox"><span class="glyphicon glyphicon-record"></span></div> '+
                            '<div class="col-sm-11">'+
                                '<div class="mdl-textfield mdl-js-textfield">'+
                                    '<input class="mdl-textfield__input" type="text" id="multiple-choice-3" name="option_mul_'+el.quesCount+'_3">'+
                                    '<label class="mdl-textfield__label" for="multiple-choice-3">Option 3</label>'+
                                '</div>'+
                            '</div>'+
                            '<div class="col-sm-1 optionBox"><span class="glyphicon glyphicon-record"></span></div> '+
                            '<div class="col-sm-11">'+
                                '<div class="mdl-textfield mdl-js-textfield">'+
                                    '<input class="mdl-textfield__input" type="text" id="multiple-choice-4" name="option_mul_'+el.quesCount+'_4">'+
                                    '<label class="mdl-textfield__label" for="multiple-choice-4">Option 4</label>'+
                                '</div>'+
                            '</div>'+
                        '</div>'+

                     '</div>'+
                '</div>');
            el.formContainer.append(multipleChoice);
        }
    };

    var eventArray = [
      {
        target  : el.shortTypeQues,
        handler : methods._getShortQuestionOptionMarkup,
        type    : 'click'
      },
      {
        target  : el.singleTypeQues,
        handler : methods._getSingleQuestionOptionMarkup,
        type    : 'click'
      },
      {
        target  : el.multipleTypeQues,
        handler : methods._getMultipleQuestionOptionMarkup,
        type    : 'click'
      }
    ];

    myEvents.attachEvent(eventArray);

    return {
        _defaults : _defaults,
        el : el,
        methods : methods
    };

})();


'use strict';

/* Directives */


angular.module('myApp.directives', [])
    .directive('appVersion', ['version', function(version) {
        return function(scope, elm, attrs) {
            elm.text(version);
        };
    }])
    .directive('tooltip', function () {
        return {
            restrict:'A',

            link: function(scope, element, attrs)
            {
                var numericDate = scope.w.fields.numericdate === null ? 0 : scope.w.fields.numericdate;
                var text = "<strong>" + scope.w.fields.title + "</strong><br/>"
                            + scope.w.pk + " d: " + numericDate
                            + '<br/> <img src="' + scope.w.fields.imageUrl + '" width=100 /><br/>';

                $(element)
                    //.attr('title',scope.$eval(attrs.tooltip))
                    .attr('title',text)
                    .tooltip({placement: "bottom", html: true, trigger: 'hover'});
            }
        }
    })
    .directive('timeline', function () {
        var timeline;
        var options = {
            'width':  '100%',
            'height':  '1000px',
            'style': 'box',
//            'animate': false,
            "min": new Date(1000, 0, 1),                // lower limit of visible range
            "max": new Date(2012, 11, 31),              // upper limit of visible range
            "zoomMin":  31556952000,                    // one year in milliseconds

//            'cluster': true,
            'scale': links.Timeline.StepDate.YEAR
        };

        return {
            restrict:'A',

            link: function(scope, element, attrs)
            {
                scope.data = [];
                scope.$watch('works', function (newValue, oldValue) {
                    console.log('scope.works: ', scope.works);
                    if (scope.works.length === 0) {
                        return;
                    }

                    angular.forEach(scope.works, function (w, idx) {
                        var numericDate = w.fields.numericdate === null ? 0 : w.fields.numericdate;
                        var timelineItem = {
                            start: new Date(numericDate, 0, 1),
                            content: '<div class="timelineSwatch" data-pk="'
                                + w.pk +
                                '" style="background-color:#'
                                + w.fields.dominantcolor[0].hex +
                                ';"><a href="'
                                + w.fields.workurl +
                                '" target="_blank"></a></div>'
                        };
                        scope.data.push(timelineItem);
                    });

                    // Instantiate our timeline object.
                    timeline = new links.Timeline(element[0]);
                    // Draw our timeline with the created data and options
                    timeline.draw(scope.data, options);
                });

            }


        }
    });
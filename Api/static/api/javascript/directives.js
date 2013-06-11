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

                var text = "<strong>" + scope.w.fields.title + "</strong><br/>"
                            + scope.w.pk
                            + '<br/> <img src="' + scope.w.fields.imageUrl + '" width=100 /><br/>';

                $(element)
                    //.attr('title',scope.$eval(attrs.tooltip))
                    .attr('title',text)
                    .tooltip({placement: "bottom", html: true, trigger: 'hover'});
            }
        }
    });
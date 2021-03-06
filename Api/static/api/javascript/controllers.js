'use strict';

/* Controllers */

angular.module('myApp.controllers', [])
    .controller('MyCtrl1', ['$scope', '$http', '$location', '$log', function($scope, $http, $location, $log) {
        var url = '/api/work/j/color';
        var pageNum = $location.search()['page'];
        $scope.works = [];
        $scope.sortorder = "default";
        $scope.currentOver = {};

        $http.get(url, {cache: true, params: {page: pageNum}})
            .success(function(data) {
                $log.debug('#', pageNum, data, data.length);
                $scope.works = data;
              })
              .error(function (data, status) {
                console.error('Error fetching feed:', data, ' ', status);
              });

        $scope.doSort = function(w) {
            var numericDate = w.fields.numericdate === null ? 0 : w.fields.numericdate;
            switch ($scope.sortorder)  {
                case "hue":
                    return w.fields.dominantcolor[0].hsv[0];
                case "saturation":
                    return w.fields.dominantcolor[0].hsv[1];
                case "brightness":
                    return w.fields.dominantcolor[0].hsv[2];
                case "date":
                    return numericDate;
                default:
                    return w.pk;
            }
        };

        $scope.overSwatch = function(w) {
            $scope.currentOver = w;
        };

  }]);
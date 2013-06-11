'use strict';

/* Controllers */

angular.module('myApp.controllers', []).
  controller('MyCtrl1', ['$scope', '$http', '$location', '$log', function($scope, $http, $location, $log) {
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
            switch ($scope.sortorder)  {
                case "hue":
                    return w.fields.dominantcolor[0].hsv[0];
                case "brightness":
                    return w.fields.dominantcolor[0].hsv[2];
                default:
                    return w.pk;
            }
        };

        $scope.overSwatch = function(w) {
            $scope.currentOver = w;
        };

  }]);
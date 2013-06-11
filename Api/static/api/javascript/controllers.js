'use strict';

/* Controllers */

angular.module('myApp.controllers', []).
  controller('MyCtrl1', ['$scope', '$http', '$location', '$log', function($scope, $http, $location, $log) {
        var url = '/api/work/j/color';
        var pageNum = $location.search()['page'];
        $scope.works = [];

        $http.get(url, {cache: true, params: {page: pageNum}})
            .success(function(data) {
                $log.debug('#', pageNum, data, data.length);
                $scope.works = data;
              })
              .error(function (data, status) {
                console.error('Error fetching feed:', data, ' ', status);
              });


  }])
  .controller('MyCtrl2', [function() {

  }]);
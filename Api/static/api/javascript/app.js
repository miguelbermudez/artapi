'use strict';

// Declare app level module which depends on filters, and services
angular.module('myApp', ['myApp.filters', 'myApp.services', 'myApp.directives', 'myApp.controllers'])
    .config(function ($logProvider, $locationProvider) {
        $locationProvider.html5Mode(true);
        $logProvider.debugEnabled(true);

    });
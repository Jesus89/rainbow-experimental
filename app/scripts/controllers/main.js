'use strict';

/**
 * @ngdoc function
 * @name rainbowClientApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the rainbowClientApp
 */
angular.module('rainbowClientApp')
    .controller('MainCtrl', function($scope, $http) {
        $scope.requestParams = {
            method: 'GET',
            url: 'http://localhost:8080'
        }

        $scope.successResponse = '';
        $scope.errorResponse = '';

        $scope.doRequest = function() {
            $http($scope.requestParams).then(function(data) {
                $scope.successResponse = JSON.stringify(data);
                $scope.errorResponse = '';
            }, function(data) {
                $scope.successResponse = '';
                $scope.errorResponse = JSON.stringify(data);
            });
        }
    });
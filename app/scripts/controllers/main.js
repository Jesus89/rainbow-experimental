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
            url: 'http://localhost:8081'
        }

        $scope.successResponse = null;
        $scope.errorResponse = null;
        $scope.successResponseText = '';
        $scope.errorResponseText = '';

        $scope.parameters = [];

        $scope.doRequest = function() {
            $http($scope.requestParams).then(function(data) {
                $scope.successResponse = data;
                $scope.successResponseText = JSON.stringify(data);
                $scope.errorResponse = null;
                $scope.errorResponseText = '';
                console.log($scope.successResponse);
            }, function(data) {
                $scope.successResponse = null;
                $scope.successResponseText = '';
                $scope.errorResponseText = JSON.stringify(data);
            });
        }

        $scope.stringify = function(object) {
            return JSON.stringify(object);
        }

        $scope.doMethodRequest = function(key) {
            var requestParams = {
                method: $scope.requestParams.method,
                url: $scope.requestParams.url + '/' + key
            };
            if (requestParams.method === 'GET') {
                requestParams.params = $scope.parameters[key];
            } else {
                requestParams.data = $scope.parameters[key];
            }

            $http(requestParams).then(function(data) {
                console.log('allOK');
                $scope.methodSuccessResponseText = JSON.stringify(data);
            }, function(data) {
                console.log('wrong');
                $scope.methodErrorResponseText = JSON.stringify(data);
                console.log(data);
            });
        }
    });
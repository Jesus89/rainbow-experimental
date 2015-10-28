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
        var ip_address = location.host.split(':')[0];
        $scope.requestParams = {
            method: 'GET',
            url: 'http://' + ip_address + ':8081'
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

        $scope.doClear = function() {
            $scope.successResponse = null
        }

        $scope.stringify = function(object) {
            return JSON.stringify(object);
        }

        $scope.doMethodRequest = function(name, key) {
            var requestParams = {
                method: $scope.requestParams.method,
                url: $scope.requestParams.url + '/' + name + '/' + key
            };
            if (requestParams.method === 'GET') {
                requestParams.params = $scope.parameters[key];
            } else {
                requestParams.data = $scope.parameters[key];
            }

            $http(requestParams).then(function(data) {
                if (data.data.status){
                    if (!!data.data.data) {
                        alert('Return: ' + data.data.data);
                    }
                } else {
                    alert('Exception: ' + data.data.message);
                }
                console.log('allOK');
                $scope.methodErrorResponseText = ''
                $scope.methodSuccessResponseText = JSON.stringify(data);
            }, function(data) {
                console.log('wrong');
                $scope.methodSuccessResponseText = ''
                $scope.methodErrorResponseText = JSON.stringify(data);
                console.log(data);
            });
        }
    });

{
   "main": {
      "modules": [
         "rainbow.modules.zum"
      ],
      "instances": {
            "zum": "rainbow.modules.zum.Zum()",
      },
      "methods": {
         "open": {
            "engine": "zum.open",
            "args": null
         },
         "close": {
            "engine": "zum.close",
            "args": null
         },
         "led": {
            "engine": "zum.led",
            "args": {
               "status": { }
            }
         }
      }
   }
}

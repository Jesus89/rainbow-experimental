# Rainbow client

Dynamic web client interface, built automatically from a Rainbow REST API.

It can be used with [Rainbow server](https://github.com/bqlabs/rainbow-server).

## Build & development

Run `grunt` for building and `grunt serve` for preview.

### Electron

Also you can use `grunt electron` to generate an [electron](https://github.com/atom/electron) distribution.

```bash
npm install electron-prebuilt -g
```

#### Run application

```bash
cd electron
npm install
electron .
```

#### Build packages

[electron-packager](https://github.com/maxogden/electron-packager) is used to build the packages.

```bash
npm install electron-packager -g
```

```bash
electron-packager electron Rainbow --platform=linux --arch=x64 --version=0.28.2
```

## Testing

Running `grunt test` will run the unit tests with karma.

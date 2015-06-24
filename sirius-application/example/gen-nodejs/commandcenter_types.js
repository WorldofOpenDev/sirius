//
// Autogenerated by Thrift Compiler (0.9.2)
//
// DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
//
var thrift = require('thrift');
var Thrift = thrift.Thrift;
var Q = thrift.Q;


var ttypes = module.exports = {};
MachineData = module.exports.MachineData = function(args) {
  this.name = null;
  this.port = null;
  if (args) {
    if (args.name !== undefined) {
      this.name = args.name;
    }
    if (args.port !== undefined) {
      this.port = args.port;
    }
  }
};
MachineData.prototype = {};
MachineData.prototype.read = function(input) {
  input.readStructBegin();
  while (true)
  {
    var ret = input.readFieldBegin();
    var fname = ret.fname;
    var ftype = ret.ftype;
    var fid = ret.fid;
    if (ftype == Thrift.Type.STOP) {
      break;
    }
    switch (fid)
    {
      case 1:
      if (ftype == Thrift.Type.STRING) {
        this.name = input.readString();
      } else {
        input.skip(ftype);
      }
      break;
      case 2:
      if (ftype == Thrift.Type.I32) {
        this.port = input.readI32();
      } else {
        input.skip(ftype);
      }
      break;
      default:
        input.skip(ftype);
    }
    input.readFieldEnd();
  }
  input.readStructEnd();
  return;
};

MachineData.prototype.write = function(output) {
  output.writeStructBegin('MachineData');
  if (this.name !== null && this.name !== undefined) {
    output.writeFieldBegin('name', Thrift.Type.STRING, 1);
    output.writeString(this.name);
    output.writeFieldEnd();
  }
  if (this.port !== null && this.port !== undefined) {
    output.writeFieldBegin('port', Thrift.Type.I32, 2);
    output.writeI32(this.port);
    output.writeFieldEnd();
  }
  output.writeFieldStop();
  output.writeStructEnd();
  return;
};

QueryType = module.exports.QueryType = function(args) {
  this.ASR = null;
  this.QA = null;
  this.IMM = null;
  if (args) {
    if (args.ASR !== undefined) {
      this.ASR = args.ASR;
    }
    if (args.QA !== undefined) {
      this.QA = args.QA;
    }
    if (args.IMM !== undefined) {
      this.IMM = args.IMM;
    }
  }
};
QueryType.prototype = {};
QueryType.prototype.read = function(input) {
  input.readStructBegin();
  while (true)
  {
    var ret = input.readFieldBegin();
    var fname = ret.fname;
    var ftype = ret.ftype;
    var fid = ret.fid;
    if (ftype == Thrift.Type.STOP) {
      break;
    }
    switch (fid)
    {
      case 1:
      if (ftype == Thrift.Type.BOOL) {
        this.ASR = input.readBool();
      } else {
        input.skip(ftype);
      }
      break;
      case 2:
      if (ftype == Thrift.Type.BOOL) {
        this.QA = input.readBool();
      } else {
        input.skip(ftype);
      }
      break;
      case 3:
      if (ftype == Thrift.Type.BOOL) {
        this.IMM = input.readBool();
      } else {
        input.skip(ftype);
      }
      break;
      default:
        input.skip(ftype);
    }
    input.readFieldEnd();
  }
  input.readStructEnd();
  return;
};

QueryType.prototype.write = function(output) {
  output.writeStructBegin('QueryType');
  if (this.ASR !== null && this.ASR !== undefined) {
    output.writeFieldBegin('ASR', Thrift.Type.BOOL, 1);
    output.writeBool(this.ASR);
    output.writeFieldEnd();
  }
  if (this.QA !== null && this.QA !== undefined) {
    output.writeFieldBegin('QA', Thrift.Type.BOOL, 2);
    output.writeBool(this.QA);
    output.writeFieldEnd();
  }
  if (this.IMM !== null && this.IMM !== undefined) {
    output.writeFieldBegin('IMM', Thrift.Type.BOOL, 3);
    output.writeBool(this.IMM);
    output.writeFieldEnd();
  }
  output.writeFieldStop();
  output.writeStructEnd();
  return;
};

File = module.exports.File = function(args) {
  this.file = '';
  this.b64format = false;
  if (args) {
    if (args.file !== undefined) {
      this.file = args.file;
    }
    if (args.b64format !== undefined) {
      this.b64format = args.b64format;
    }
  }
};
File.prototype = {};
File.prototype.read = function(input) {
  input.readStructBegin();
  while (true)
  {
    var ret = input.readFieldBegin();
    var fname = ret.fname;
    var ftype = ret.ftype;
    var fid = ret.fid;
    if (ftype == Thrift.Type.STOP) {
      break;
    }
    switch (fid)
    {
      case 1:
      if (ftype == Thrift.Type.STRING) {
        this.file = input.readString();
      } else {
        input.skip(ftype);
      }
      break;
      case 2:
      if (ftype == Thrift.Type.BOOL) {
        this.b64format = input.readBool();
      } else {
        input.skip(ftype);
      }
      break;
      default:
        input.skip(ftype);
    }
    input.readFieldEnd();
  }
  input.readStructEnd();
  return;
};

File.prototype.write = function(output) {
  output.writeStructBegin('File');
  if (this.file !== null && this.file !== undefined) {
    output.writeFieldBegin('file', Thrift.Type.STRING, 1);
    output.writeString(this.file);
    output.writeFieldEnd();
  }
  if (this.b64format !== null && this.b64format !== undefined) {
    output.writeFieldBegin('b64format', Thrift.Type.BOOL, 2);
    output.writeBool(this.b64format);
    output.writeFieldEnd();
  }
  output.writeFieldStop();
  output.writeStructEnd();
  return;
};

QueryData = module.exports.QueryData = function(args) {
  this.audioFile = null;
  this.textFile = null;
  this.imgFile = null;
  if (args) {
    if (args.audioFile !== undefined) {
      this.audioFile = args.audioFile;
    }
    if (args.textFile !== undefined) {
      this.textFile = args.textFile;
    }
    if (args.imgFile !== undefined) {
      this.imgFile = args.imgFile;
    }
  }
};
QueryData.prototype = {};
QueryData.prototype.read = function(input) {
  input.readStructBegin();
  while (true)
  {
    var ret = input.readFieldBegin();
    var fname = ret.fname;
    var ftype = ret.ftype;
    var fid = ret.fid;
    if (ftype == Thrift.Type.STOP) {
      break;
    }
    switch (fid)
    {
      case 1:
      if (ftype == Thrift.Type.STRUCT) {
        this.audioFile = new ttypes.File();
        this.audioFile.read(input);
      } else {
        input.skip(ftype);
      }
      break;
      case 2:
      if (ftype == Thrift.Type.STRUCT) {
        this.textFile = new ttypes.File();
        this.textFile.read(input);
      } else {
        input.skip(ftype);
      }
      break;
      case 3:
      if (ftype == Thrift.Type.STRUCT) {
        this.imgFile = new ttypes.File();
        this.imgFile.read(input);
      } else {
        input.skip(ftype);
      }
      break;
      default:
        input.skip(ftype);
    }
    input.readFieldEnd();
  }
  input.readStructEnd();
  return;
};

QueryData.prototype.write = function(output) {
  output.writeStructBegin('QueryData');
  if (this.audioFile !== null && this.audioFile !== undefined) {
    output.writeFieldBegin('audioFile', Thrift.Type.STRUCT, 1);
    this.audioFile.write(output);
    output.writeFieldEnd();
  }
  if (this.textFile !== null && this.textFile !== undefined) {
    output.writeFieldBegin('textFile', Thrift.Type.STRUCT, 2);
    this.textFile.write(output);
    output.writeFieldEnd();
  }
  if (this.imgFile !== null && this.imgFile !== undefined) {
    output.writeFieldBegin('imgFile', Thrift.Type.STRUCT, 3);
    this.imgFile.write(output);
    output.writeFieldEnd();
  }
  output.writeFieldStop();
  output.writeStructEnd();
  return;
};


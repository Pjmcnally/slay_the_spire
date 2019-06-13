var btoa = require('btoa');
var atob = require('atob');

convertToByteArray = (data) => {
    let byte_array = [];

    for (let i = 0; i < data.length; i++){
        byte_array.push(data.charCodeAt(i));
    }

    return byte_array
};

xorWithKey = (data, key) => {
    let out = [];
    data = this.convertToByteArray(data);
    key = this.convertToByteArray(key);

    for(let i = 0; i < data.length; i++) {
        out.push(String.fromCharCode(data[i] ^ key[i % key.length]));
    }

    return out.join('');
};

encrypt = (data) => {
  try {
    const decrypted = JSON.stringify(data);
    let encrypted = btoa(this.xorWithKey(decrypted, "key"));
    return encrypted;
  } catch(e) {
    console.log(e);
    alert('Invalid Base64')
  }
};


decrypt = (encrypted) => {
  try {
    let decrypted = this.xorWithKey(atob(encrypted), "key");
    return JSON.parse(decrypted);
  } catch(e) {
    console.log(e);
    alert('Invalid Base64')
  }
}

var json = decrypt(data)
console.log(json)
json.has_sapphire_key = true
console.log(encrypt(json))

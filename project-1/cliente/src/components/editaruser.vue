<template>
<div class="container">
  <div class="main">
    <div class="main-login main-center">
      <form class="form-horizontal">
        <div class="panel-title text-center">
          <h1 class="title">Edit User</h1>
          <hr />
        </div>
        <div class="form-group">
          <label for="name" class="cols-sm-2 close-bottom control-label">Your Username</label>
          <div class="cols-sm-10">
            <div class="input-group">
              <span class="input-group-addon"><i class="fa fa-user fa" aria-hidden="true"></i></span>
              <input type="text" class="form-control" v-model="username" name="name" id="name"  placeholder="Enter your Name" disabled/>
            </div>
          </div>
        </div>

        <div class="form-group">
          <label for="name" class="cols-sm-2 close-bottom control-label">Your Name</label>
          <div class="cols-sm-10">
            <div class="input-group">
              <span class="input-group-addon"><i class="fa fa-user fa" aria-hidden="true"></i></span>
              <input type="text" class="form-control" v-model="name" name="name" id="name"  placeholder="Enter your Name"/>
            </div>
          </div>
        </div>

        <div class="form-group">
          <label for="email" class="cols-sm-2 close-bottom control-label">Your Email</label>
          <div class="cols-sm-10">
            <div class="input-group">
              <span class="input-group-addon"><i class="fa fa-envelope fa" aria-hidden="true"></i></span>
              <input type="text" class="form-control" v-model="email" name="email" id="email"  placeholder="Enter your Email"/>
            </div>
          </div>
        </div>

        <div class="form-group">
          <label for="password" class="cols-sm-2 close-bottom control-label">Password</label>
          <div class="cols-sm-10">
            <div class="input-group">
              <span class="input-group-addon"><i class="fa fa-lock fa-lg" aria-hidden="true"></i></span>
              <input type="password" class="form-control" v-model="currentPass" name="currentPassword" id="currentPassword"  placeholder="Enter your Password"/>
            </div>
          </div>
        </div>

        <div class="form-group">
          <label for="confirm" class="cols-sm-2 close-bottom control-label">Confirm Password</label>
          <div class="cols-sm-10">
            <div class="input-group">
              <span class="input-group-addon"><i class="fa fa-lock fa-lg" aria-hidden="true"></i></span>
              <input type="password" class="form-control" v-model="confirmPass" name="confirm" id="confirm"  placeholder="Confirm your Password"/>
            </div>
          </div>
        </div>

        <div class="form-group separate">
          <div v-if="this.validationFail == true" class="warning">
            <label class="msg"> {{message}} </label>
          </div>
          <div v-if="this.operationSuccess == true" class="success">
            <label class="msg"> {{message}} </label>
          </div>
        </div>

        <div class="form-group ">
          <button type="button" @click="confirm" name="confirmBtn" id="confirmBtn" class="btn btn-primary btn-lg btn-block login-button">Confirm</button>
        </div>
        <div class="login-register">
          <button type="button" @click="cancel" name="confirmBtn" id="confirmBtn" class="btn btn-danger btn-lg btn-block login-button">Cancel</button>
        </div>
      </form>
    </div>
  </div>
</div>
</template>

<script>
import axios from 'axios'
export default {

  props: [ 'userProp', 'validated' ],

  data () {
    return {
      name: '',
      email: '',
      currentPass: '',
      confirmPass: '',
      username: '',
      comments: [],

      message: '',

      validationFail: false,
      operationSuccess: false
    }
  },

  created: function () {
    if (this.validated === false) { this.$router.replace({name: 'login'}) }
    this.username = this.userProp

    axios.post('http://avillada.dis.eafit.edu.co/api/v1.0/mainpage/editUser', {
      'username': this.username})

      .then((respuestaServer) => {
        this.name = respuestaServer.data[0]
        this.currentPass = respuestaServer.data[1]
        this.email = respuestaServer.data[2]
      })

      .catch((error) => { console.error(error); this.mensaje = error })
  },

  methods: {
    cancel () {
      var r = confirm('Are you sure you want to cancel the user edition?')
      if (r === true) { this.$router.replace({name: 'mainpage', params: {userProp: this.username, validated: true}}) }
    },
    confirm () {
      if (this.name.toString() === '' || this.currentPass.toString() === '' || this.email.toString() === '') { this.validationFail = true; this.operationSuccess = false; this.message = 'All spaces are required'; return 1 }
      if (this.currentPass.toString() !== this.confirmPass.toString()) { this.validationFail = true; this.operationSuccess = false; this.message = 'The passwords entered do not match'; return 1 }
      var r = confirm('Are you sure you want to edit your profile?')
      if (r === false) { return 1 }

      axios.post('http://avillada.dis.eafit.edu.co/api/v1.0/mainpage/editUser/confirm', {

        'name': this.name.trim(),
        'email': this.email.trim(),
        'username': this.username.trim(),
        'password': this.currentPass.trim() })

        .then((respuestaServer) => {
          if (respuestaServer.data === true) { this.validationFail = false; this.operationSuccess = true; this.message = 'The user was edited successfully'; this.confirmPass = '' } else { this.validationFail = true; this.operationSuccess = true; this.message = 'There was a problem to edit your profile' }
        })

        .catch((error) => { console.error(error); this.mensaje = error })
    }
  }
}
</script>

<style lang='css' scoped>
body, html{
  height: 100%;
   background-repeat: no-repeat;
   background-color: #d3d3d3;
   font-family: 'Oxygen', sans-serif;
}

.main{
   margin-top: 70px;
}

h1.title {
  font-size: 50px;
  font-family: 'Passion One', cursive;
  font-weight: 400;
}

hr{
  width: 10%;
  color: #fff;
}

.form-group{
  margin-bottom: 15px;
}

label{
  margin-bottom: 15px;
}

input,
input::-webkit-input-placeholder {
  font-size: 11px;
  padding-top: 3px;
}

.main-login{
   background-color: #fff;
  /* shadows and rounded borders */
  -moz-border-radius: 2px;
  -webkit-border-radius: 2px;
  border-radius: 2px;
  -moz-box-shadow: 0px 2px 2px rgba(0, 0, 0, 0.3);
  -webkit-box-shadow: 0px 2px 2px rgba(0, 0, 0, 0.3);
  box-shadow: 0px 2px 2px rgba(0, 0, 0, 0.3);

}

.main-center{
  margin-top: 30px;
  margin: 0 auto;
  max-width: 430px;
  padding: 40px 40px;

}

.login-button{
  margin-top: 5px;
}

.login-register{
  font-size: 11px;
  text-align: center;
}
.info, .success, .warning, .error, .validation {
  margin: 0 auto;
  margin-top: 10px;
  border: 1px solid;
  padding: 15px 10px 15px 50px;
  background-repeat: no-repeat;
  background-position: 10px center;
  max-width:300%;
}
.info {
  color: #00529B;
  background-color: #BDE5F8;
  background-image: url('https://i.imgur.com/ilgqWuX.png');
}
.success {
  color: #4F8A10;
  background-color: #DFF2BF;
  background-image: url('https://i.imgur.com/Q9BGTuy.png');
}
.warning {
  color: #9F6000;
  background-color: #FEEFB3;
  background-image: url('https://i.imgur.com/Z8q7ww7.png');
}
.error{
  color: #D8000C;
  background-color: #FFBABA;
  background-image: url('https://i.imgur.com/GnyDvKN.png');
}
.validation{
  color: #D63301;
  background-color: #FFCCBA;
  background-image: url('https://i.imgur.com/GnyDvKN.png');
}
.msg {
  margin: 0 auto;
  margin-left: -50px;
  font-size: 11px;
}
.close-bottom {
  margin-bottom: -10px;
}
.separate {
  margin-top: 10px;
  margin-bottom: 10px;
}

</style>

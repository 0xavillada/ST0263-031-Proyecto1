<template>
<div class="container">
  <div class="main">
    <div class="main-login main-center">
      <form class="form-horizontal">
        <h1 class="title">Register User</h1>
        <div class="form-group">
          <label for="name" class="separate control-label">Your Name</label>
          <div class="cols-sm-10">
            <div class="input-group">
              <span class="input-group-addon"><i class="fa fa-user fa" aria-hidden="true"></i></span>
              <input type="text" class="form-control" name="name" id="name" v-model="nameEntered" placeholder="Enter your Name"/>
            </div>
          </div>
        </div>

        <div class="form-group">
          <label for="email" class="separate control-label">Your Email</label>
          <div class="cols-sm-10">
            <div class="input-group">
              <span class="input-group-addon"><i class="fa fa-envelope fa" aria-hidden="true"></i></span>
              <input type="text" class="form-control" name="email" id="email" v-model="emailEntered" placeholder="Enter your Email"/>
            </div>
          </div>
        </div>

        <div class="form-group">
          <label for="username" class="separate control-label">Username</label>
          <div class="cols-sm-10">
            <div class="input-group">
              <span class="input-group-addon"><i class="fa fa-users fa" aria-hidden="true"></i></span>
              <input type="text" class="form-control" name="username" id="username" v-model="usernameEntered" placeholder="Enter your Username"/>
            </div>
          </div>
        </div>

        <div class="form-group">
          <label for="password" class="separate control-label">Password</label>
          <div class="cols-sm-10">
            <div class="input-group">
              <span class="input-group-addon"><i class="fa fa-lock fa-lg" aria-hidden="true"></i></span>
              <input type="password" class="form-control" name="password" id="password" v-model="passwordEntered" placeholder="Enter your Password"/>
            </div>
          </div>
        </div>

        <div class="form-group">
          <label for="confirm" class="separate control-label">Confirm Password</label>
          <div class="cols-sm-10">
            <div class="input-group">
              <span class="input-group-addon"><i class="fa fa-lock fa-lg" aria-hidden="true"></i></span>
              <input type="password" class="form-control" name="confirm" id="confirm" v-model="confirmEntered" placeholder="Confirm your Password"/>
            </div>
          </div>
        </div>

        <div class="form-group separate">
          <div v-if="this.validationFail == true" class="validation">
            <label class="msg"> {{message}} </label>
          </div>
          <div v-if="this.nullEntry == true" class="warning">
            <label class="msg"> {{message}} </label>
          </div>
        </div>

        <form @submit.prevent="respuestaUser">
          <div class="form-group ">
            <button type="submit" name="registerBtn" id="registerBtn" class="separate-top btn btn-primary btn-lg btn-block login-button">Register</button>
          </div>
        </form>

        <div class="login-register">
          <a href="/">Do you already have an account? Login here</a>
        </div>

      </form>
    </div>
  </div>
</div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Register',

  data () {
    return {
      nameEntered: '',
      emailEntered: '',
      usernameEntered: '',
      passwordEntered: '',
      confirmEntered: '',

      message: '',
      validationFail: false,
      nullEntry: false,

      respuesta: false
    }
  },

  methods: {

    respuestaUser () {
      if (this.entradaVacia() === true) { this.message = 'All spaces are required'; this.validationFail = false; this.nullEntry = true } else { this.confirmPass() }
    },

    entradaVacia () {
      if (this.nameEntered.trim() === '' || this.emailEntered.trim() === '' || this.usernameEntered.trim() === '' || this.passwordEntered.trim() === '' || this.confirmEntered.trim() === '') { return true } else { return false }
    },

    confirmPass () {
      if (this.passwordEntered.trim() === this.confirmEntered.trim()) { this.validar() } else { this.message = 'The passwords entered do not match'; this.validationFail = true; this.nullEntry = false }
    },

    validar () {
      axios.post('http://avillada.dis.eafit.edu.co/api/v1.0/register', {

        'name': this.nameEntered.trim(),
        'email': this.emailEntered.trim(),
        'username': this.usernameEntered.trim(),
        'password': this.passwordEntered.trim() })

        .then((respuestaServer) => {
          this.respuesta = respuestaServer.data
          this.registro()
        })

        .catch((error) => { console.error(error); this.mensaje = error })
    },

    registro () {
      if (this.respuesta === true) { alert('The user was created successfully'); this.$router.replace({name: 'login'}) } else { this.message = 'that user is already registered'; this.validationFail = true; this.nullEntry = false }
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
  margin-bottom: 40px;
}
hr{
  width: 10%;
  color: #fff;
}
.form-group{
  margin-top: -20px;
  margin-bottom: 25px;
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
  margin-top: 50px;
  font-size: 11px;
  text-align: center;
}
.info, .success, .warning, .error, .validation {
  border: 1px solid;
  margin: 10px 0px;
  padding: 15px 10px 15px 50px;
  background-repeat: no-repeat;
  background-position: 10px center;
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
.msg{
  margin: 0 auto;
  margin-left: -50px;
  font-size: 11px;
}
.separate-top {
  margin-top: 50px;
  margin-bottom: 50px;
}

.separate {
  margin-top: 10px;
  margin-bottom: -10px;
}

</style>

<template>
<div class="container">
  <div class="main">
    <div class="main-login main-center">
      <form class="form-horizontal" method="post" action="#">
        <!-- -->
        <form @submit.prevent="respuestaUser">
          <h1 class="title">Login</h1>
          <div class="form-group">
            <label for="username" class="separate">Username</label>
            <div class="cols-sm-10">
              <div class="input-group">
                <span class="input-group-addon"><i class="fa fa-users fa" aria-hidden="true"></i></span>
                <input type="text" class="form-control" name="username" id="username" v-model="usernameEntered" placeholder="Enter your Username"/>
              </div>
            </div>
          </div>

          <div class="form-group">
            <label for="password" class="separate">Password</label>
            <div class="cols-sm-10">
              <div class="input-group">
                <span class="input-group-addon"><i class="fa fa-lock fa-lg" aria-hidden="true"></i></span>
                <input type="password" class="form-control" name="password" id="password" v-model="passwordEntered" placeholder="Enter your Password"/>
              </div>
            </div>
          </div>

          <div class="form-group ">
            <button type="submit" name="loginBtn" id="loginBtn" class="btn btn-primary separate-top btn-lg btn-block login-button">Log in</button>
            <div v-if="this.validationFail == true" class="validation">
              <label class="msg"> Incorrect user or password </label>
            </div>
            <div v-if="this.nullEntry == true" class="warning">
              <label class="msg"> All spaces are required </label>
            </div>
          </div>
        </form>
        <!-- -->
        <div class="login-register">
                <a href="/register">You don't have an account yet? Sign up here</a>
              </div>
      </form>
    </div>
  </div>
</div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Login',

  data () {
    return {
      usernameEntered: '',
      passwordEntered: '',
      validationFail: false,
      nullEntry: false,
      respuesta: false,

      userProp: ''
    }
  },

  methods: {

    respuestaUser () {
      if (this.entradaVacia() === true) { this.validationFail = false; this.nullEntry = true } else { this.validar() }
    },

    entradaVacia () {
      if (this.usernameEntered.trim() === '' || this.passwordEntered.trim() === '') { return true } else { return false }
    },

    validar () {
      axios.post('http://localhost:5000/api/v1.0/login', {
        'username': this.usernameEntered.trim(),
        'password': this.passwordEntered.trim() })

        .then((respuestaServer) => {
          this.respuesta = respuestaServer.data
          this.ingreso()
        })

        .catch((error) => { console.error(error); this.mensaje = error })
    },

    ingreso () {
      if (this.respuesta === true) { this.redirect() } else { this.validationFail = true; this.nullEntry = false }
    },

    redirect () {
      this.$router.replace({name: 'mainpage', params: {userProp: this.usernameEntered, validated: true}})
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
  padding: 30px 30px;

}

.login-button{
  margin-top: 5px;
}

.login-register{
  margin-top: 60px;
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
}

.separate {
  margin-top: 10px;
  margin-bottom: -10px;
}

</style>

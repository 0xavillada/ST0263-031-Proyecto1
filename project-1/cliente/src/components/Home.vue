<template lang='html'>
<div id="login">
    <div class="container">
        <div id="login-row" class="row justify-content-center align-items-center">
            <div id="login-column" class="col-md-6">
                <div id="login-box" class="col-md-12">
                    <form id="login-form" class="form" action="" method="post">
                        <h3 class="text-center text-info">Login</h3>
                        <div class="form-group">
                            <label for="username" class="text-info">Username:</label><br>
                            <input type="text" name="username" id="username" class="form-control">
                        </div>
                        <div class="form-group">
                          <label for="password" class="text-info">Password:</label><br>
                            <input type="text" name="password" id="password" class="form-control">
                        </div>
                        <div class="form-group">
                          <label for="remember-me" class="text-info"><span>Remember me</span><span><input id="remember-me" name="remember-me" type="checkbox"></span></label><br>
                            <input type="submit" name="submit" class="btn btn-info btn-md" value="submit">
                        </div>
                        <div id="register-link" class="text-right">
                            <a href="#" class="text-info">Register here</a>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
</div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Main',
  data () {
    return {
      mensaje: 'algo aqui'
    }
  },
  methods: {
    getMensaje () {
      const path = 'http://localhost:5000/api/v1.0/login'
      axios.get(path).then((respuesta) => {
        this.mensaje = respuesta.data
      })
        .catch((error) => {
          console.error(error)
        })
    },
    test () {
      this.mensaje = 'nuevo esto'
    }
  },
  created () {
    this.getMensaje()
    this.test()
    this.head()
  }
}

</script>

<style lang='css' scoped>
body {
  margin: 0 auto;
  padding: 0;
  background-color: #17a2b8;
  height: 100vh;
}
#login .container #login-row #login-column #login-box {
  margin: 0 auto;
  margin-top: 120px;
  max-width: 600px;
  height: 320px;
  border: 1px solid #9C9C9C;
  background-color: #EAEAEA;
}
#login .container #login-row #login-column #login-box #login-form {
  margin: 0 auto;
  padding: 20px;
}
#login .container #login-row #login-column #login-box #login-form #register-link {
  margin: 0 auto;
  margin-top: 20px;
}

</style>

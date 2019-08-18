<template>
<div class="container-fluid">
  <div>
    <div class="main-login main-center">
      <div class="separate">
        <div>
          <h1 class="text-center">Project 1</h1>
          <h3 class="separate-bottom">
            Main Page
          </h3>
        </div>
      </div>
      <div>
        <div>
            <div id="comment-list" class="container">
              <div>
                <h1 class="text-center"></h1>
                <div class="mx-auto text-left">
                  <form v-on:submit.prevent="updateComment">
                    <div>
                      <dl>
                      <label class="text-left" for="commentInput">{{'Username: "' + username + '"'}} </label>
                      <a class="text-right" href="/">log out</a>
                      <button type="button" @click="editUser" name="editUserBtn" id="editUserBtn" class="btn btn-success separate-left text-right">
                        Edit User
                      </button>
                    </dl>
                      <label class="text-center" for="commentInput">Theme: </label>
                    </div>
                    <input v-model="themeEntered" class="" type="text" id="themeInput" placeholder="#Theme">
                    <div class="text-left">
                      <label class="text-center separate-top" for="commentInput">Comment: </label>
                      <p><textarea v-model="commentEntered" type="text" id="commentInput" class="text-response" placeholder="What do you think?">
                      </textarea></p>
                    </div>
                    <div>
                      <div v-if="this.validationFail == true" class="warning text-center">
                        <label class="msg"> All spaces are required </label>
                      </div>
                      <div v-if="this.operationSuccess == true" class="success text-center">
                        <label class="msg"> {{message}} </label>
                      </div>
                    </div>
                      <button type="button" v-on:click="newComment" class="btn btn-primary mt-3">
                        Comment
                      </button>
                  </form>
                  <table class="table">
                    <div class="text-left separate-top">
                      <label class="text-right" for="commentInput">Search:</label>
                      <input v-model="searchEntered" type="text" id="searchInput" class="separate" placeholder="Search comments">
                    </div>
                    <div class="text-left separate">
                      <label class="text-right" for="commentInput">Find by: </label>
                      <button v-on:click="searchByTheme" class="btn btn-info">#Theme</button>
                      <button v-on:click="searchByUser" class="btn btn-info">@Username</button>
                      <button v-on:click="searchByMine" class="btn btn-info">Mine</button>
                      <button v-on:click="searchByLatest" class="btn btn-info">Latest</button>
                    </div>
                    <div v-if="this.isEdit == true" class="text-left">
                      <input v-model="themeEditing" type="text" disabled>
                    </div>
                    <div v-if="this.isEdit == true" class="text-left">
                      <p><textarea v-model="commentEditing" type="text" class="form-control" cols="60" >
                      </textarea></p>
                    </div>
                    <div v-if="this.isEdit == true" class="text-left">
                      <button v-on:click="updateComment" class="btn btn-success separate">Edit comment</button>
                      <button v-on:click="cancelEdit" class="btn btn-danger separate">Cancel</button>
                    </div>
                    <tr v-for="(one_comment, index) in comments" v-bind:key="index">
                      <td class="text-left">{{'@'+one_comment[0]+'\n'+'#'+one_comment[1]+" '"+one_comment[2]+"'"}}</td>
                      <td class="text-right" v-if="one_comment[0].toString() === username.toString()">
                        <button v-on:click="editComment(one_comment)" class="btn btn-info">Edit</button>
                        <button v-on:click="confirmDelete(one_comment)" class="btn btn-danger">Delete</button>
                      </td>
                    </tr>
                  </table>
                </div>
              </div>
            </div>
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import axios from 'axios'
export default {
  // name: 'mainpage',

  props: [ 'userProp', 'validated' ],

  data () {
    return {
      username: '',
      comments: [],

      message: '',

      tableState: 'all',

      isEdit: false,
      themeEditing: '',
      commentEditing: '',
      indexInUser: 0,

      commentEntered: '',
      themeEntered: '',
      searchEntered: '',
      validationFail: false,
      operation: false,
      operationSuccess: false
    }
  },

  created: function () {
    if (this.validated === true) { this.username = this.userProp; this.init() } else { this.$router.replace({name: 'login'}) }
  },

  methods: {

    init () {
      // aqui ya se encuentra validado
      if (this.tableState.toString() === 'theme'.toString()) { this.listByTheme(); return 1 }
      axios.post('http://avillada.dis.eafit.edu.co/api/v1.0/mainpage', {
        'criterio': this.tableState })

        .then((respuestaServer) => {
          this.comments = respuestaServer.data
          // this.ingreso()
        })

        .catch((error) => { console.error(error); this.mensaje = error })
    },

    newComment () {
      this.validationFail = false; this.operationSuccess = false
      if (this.entradaVacia() === true) { this.validationFail = true; this.operationSuccess = false } else { this.validationFail = false; this.addComment() }
    },

    entradaVacia () {
      if (this.commentEntered.trim() === '' || this.themeEntered.trim() === '') { return true } else { return false }
    },

    addComment () {
      axios.post('http://avillada.dis.eafit.edu.co/api/v1.0/mainpage/addComment', {
        'username': this.username,
        'theme': this.themeEntered,
        'text': this.commentEntered.trim() })

        .then((respuestaServer) => {
          this.operation = respuestaServer.data
          this.validationFail = false; this.operationSuccess = true
          this.message = 'Comment added successfully'
          this.themeEntered = ''; this.commentEntered = ''
          this.init()
        })

        .catch((error) => { console.error(error); this.mensaje = error })
    },
    searchByTheme () {
      this.validationFail = false; this.operationSuccess = false
      if (this.searchEntered.trim() === '') { } else { this.listByTheme() }
    },

    listByTheme () {
      axios.post('http://avillada.dis.eafit.edu.co/api/v1.0/mainpage/byTheme', {
        'theme': this.searchEntered })

        .then((respuestaServer) => {
          this.comments = respuestaServer.data
          this.tableState = 'theme'
        })

        .catch((error) => { console.error(error); this.mensaje = error })
    },

    searchByUser () {
      this.validationFail = false; this.operationSuccess = false
      if (this.searchEntered.trim() === '') { } else { this.tableState = this.searchEntered; this.init() }
    },

    searchByMine () {
      this.validationFail = false; this.operationSuccess = false
      this.tableState = this.username
      this.searchEntered = ''
      this.init()
    },

    searchByLatest () {
      this.validationFail = false; this.operationSuccess = false
      this.tableState = 'all'
      this.searchEntered = ''
      this.init()
    },

    editComment (comment) {
      this.validationFail = false; this.operationSuccess = false
      this.themeEditing = comment[1]
      this.commentEditing = comment[2]
      this.indexInUser = comment[3]
      this.isEdit = true
    },

    confirmDelete (comment) {
      var r = confirm('Are you sure you want to delete this comment?')
      if (r === true) { this.deleteComment(comment) }
    },

    deleteComment (comment) {
      this.validationFail = false; this.operationSuccess = false
      axios.post('http://avillada.dis.eafit.edu.co/api/v1.0/mainpage/deleteComment', {
        'username': comment[0].toString(),
        'theme': comment[1].toString(),
        'text': comment[2].toString().trim() })

        .then((respuestaServer) => {
          this.operation = respuestaServer.data
          if (this.operation === false) { alert('We have a problem to delete that comment!'); return 1 }
          alert('The comment was deleted successfully!')
          this.init()
        })

        .catch((error) => { console.error(error); this.mensaje = error })
    },
    updateComment () {
      var r = confirm('Are you sure you want to edit this comment?')
      if (r === false) { return 1 }
      axios.post('http://avillada.dis.eafit.edu.co/api/v1.0/mainpage/editComment', {
        'username': this.username.toString(),
        'theme': this.themeEditing.toString(),
        'indexInUser': this.indexInUser,
        'text': this.commentEditing.toString().trim() })

        .then((respuestaServer) => {
          this.operation = respuestaServer.data
          if (this.operation === false) { alert('We have a problem to delete that comment!'); return 1 }
          alert('The comment was edited successfully!')
          this.cancelEdit()
          this.init()
        })

        .catch((error) => { console.error(error); this.mensaje = error })
    },
    cancelEdit () {
      this.themeEditing = ''
      this.commentEditing = ''
      this.indexInUser = 0
      this.isEdit = false
    },
    editUser () {
      this.$router.replace({name: 'editaruser', params: {userProp: this.username, validated: true}})
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
  max-width: 1000px;
  padding: 40px;
}

.login-button{
  margin-top: 5px;
}

.login-register{
  font-size: 11px;
  text-align: center;
}

.table{
  margin: 0 auto;
  margin-top: 20px;
}

.text-left{
  text-align: left;
  margin-right: 200px;
}

.text-right{
  text-align: right;
}

.separate{
  margin-bottom: 20px;
}

.text-center{
  margin: 0 auto;
}

.separate-right{
  margin-right: 40px;
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
.separate-bottom {
  margin-bottom: 50px;
}
.separate-left {
  margin-left: 30px;
}
.separate-top {
  margin-top: 20px;
}
.text-response {
  width: calc(100%);
  height: auto;
}
</style>

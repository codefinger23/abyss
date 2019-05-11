<template>
<div class="ui middle aligned center aligned grid">
  <div class="column">
    <h2 class="ui teal image header">
      <img src="@/assets/logo.png" class="image">
      <div class="content">
        注册账号
      </div>
    </h2>
    <form class="ui large form">
      <div class="ui stacked segment">
        <div class="field">
          <div class="ui left icon input">
            <i class="mail icon"></i>
            <input type="text" name="email" placeholder="邮箱地址" v-model="user.email">
          </div>
        </div>
        <div class="field">
          <div class="ui left icon input">
            <i class="user icon"></i>
            <input type="text" name="nickname" placeholder="昵称" v-model="user.nickname">
          </div>
        </div>
        <div class="field">
          <div class="ui left icon input">
            <i class="lock icon"></i>
            <input type="password" name="password" placeholder="密码" v-model="user.password">
          </div>
        </div>
        <div class="field">
          <div class="ui left icon input">
            <i class="barcode icon"></i>
            <input type="text" name="invite" placeholder="邀请码" v-model="user.invite">
          </div>
        </div>
        <div class="ui fluid large teal submit button">注册</div>
      </div>

      <div class="ui error message"></div>

    </form>

    <div class="ui message">
      已有账户？ <router-link to="/signin">登录</router-link>
    </div>
  </div>
</div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      user: {
        email: "",
        nickname: "",
        password: "",
        invite: ""
      },
      fields: {
        email: {
          identifier  : 'email',
          rules: [{
            type   : 'empty',
            prompt : '请输入邮箱账号'
          },{
            type   : 'email',
            prompt : '请输入合法的邮箱'
          }]
        },
        password: {
          identifier  : 'password',
          rules: [{
            type   : 'empty',
            prompt : '请输入密码'
          },{
            type   : 'length[6]',
            prompt : '密码最少6个字符'
          }]
        },
        nickname: {
          identifier  : 'nickname',
          rules: [{
            type   : 'empty',
            prompt : '请输入昵称'
          },{
            type   : 'maxLength[12]',
            prompt : '昵称最多12个字符'
          }]
        },
        invite: {
          identifier  : 'invite',
          rules: [{
            type   : 'empty',
            prompt : '请输入邀请码'
          }]
        },
      }
    }
  },
  methods: {
    bindsubmit() {
      console.log("Hello World!");
      let _self = this;
      let d = {
        "account": _self.user.email,
        "password": _self.user.password,
        "nickname": _self.user.nickname,
        "invite": _self.user.invite
      }
      api.auth.save(d).then(
        function(response) {
          console.log(response);
          $('.ui.form').form('add prompt', "email", "邮箱已存在");
          $('.ui.form').form('add prompt', "invite", "邀请码不可用");
          // $('.ui.form').form('add errors', ["邮箱已经存在"]);
        },
        function(response) {
          $('.ui.form').form('add errors', ["发生未知错误！！！"]);
        }
      )
      return false
    },
    init() {
      let _self = this;
      $('.ui.form').form({
          fields: _self.fields,
          inline: true,
          onSuccess: _self.bindsubmit
        });
    }
  },
  mounted() {
    this.init();
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.column {
    max-width: 450px;
}
#app > .grid {
    height: 100%;
    background-color: #DADADA;
}
</style>

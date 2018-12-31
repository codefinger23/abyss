<template>
<div class="ui middle aligned center aligned grid">
  <div class="column">
    <h2 class="ui teal image header">
      <img src="@/assets/logo.png" class="image">
      <div class="content">
        登录到账号
      </div>
    </h2>
    <form class="ui large form">
      <div class="ui stacked segment">
        <div class="field">
          <div class="ui left icon input">
            <i class="user icon"></i>
            <input type="text" name="email" placeholder="邮箱地址">
          </div>
        </div>
        <div class="field">
          <div class="ui left icon input">
            <i class="lock icon"></i>
            <input type="password" name="password" placeholder="密码">
          </div>
        </div>
        <div class="ui fluid large teal submit button">登录</div>
      </div>

      <div class="ui error message"></div>

    </form>

    <div class="ui message">
      新用户？ <a href="login.php#">注册</a>
    </div>
  </div>
</div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      fields: {
        email: {
          identifier  : 'email',
          rules: [{
            type   : 'empty',
            prompt : 'Please enter your e-mail'
          },{
            type   : 'email',
            prompt : 'Please enter a valid e-mail'
          }]
        },
        password: {
          identifier  : 'password',
          rules: [{
            type   : 'empty',
            prompt : 'Please enter your password'
          },{
            type   : 'length[6]',
            prompt : 'Your password must be at least 6 characters'
          }]
        }
      }
    }
  },
  methods: {
    bindsubmit() {
      console.log("Hello World!");
      console.log($('.ui.form').form("clear"));
      return false
    },
    init() {
      let _self = this;
      $('.ui.form').form({
          fields: _self.fields,
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

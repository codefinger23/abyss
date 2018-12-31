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
      msg: 'Welcome to Your Vue.js App'
    }
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

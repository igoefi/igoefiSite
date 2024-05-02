<template>
  <div id="wrapper">
    <nav class="navbar is-dark">
      <div class="navbar-brand">
        <RouterLink to="/" class="navbar-item"><strong>Igoefi</strong></RouterLink>
        <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu" @click="showMobileMenu = !showMobileMenu">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <div class="navbar-menu" id="navbar-menu" v-bind:class="{'is-active': showMobileMenu}">

        <div class="navbar-start">
          <div class="navbar-item">
            <form method="get" action="/search">
              <div class="field has-addons">
                <div class="control">
                  <input type="text" class="input" placeholder="Search" name="query">
                </div>

                <div class="control">
                  <button class="button is-success">
                      <span class="icon">
                      <i class="fas fa-search"></i>
                      </span>
                  </button>
                </div>
              </div>
            </form>
          </div>
        </div>
        
        <div class="navbar-end">
          <RouterLink to="/summer" class="navbar-item">Summer</RouterLink>
          <RouterLink to="/winter" class="navbar-item">Winter</RouterLink>
          <RouterLink to="/coffee" class="navbar-item">Coffee</RouterLink>

          <div class="navbar-item">
            <div class="buttons">
              <RouterLink to="/cart" class="button is-success">
                <span class="icon"><i class="fas fa-shopping-cart"></i></span>
                <span>Cart ({{ cartTotalLength }})</span>
              </RouterLink>
            </div>
          </div>
        </div>
      </div>
    </nav>

    <section class="section">
      <RouterView/>
    </section>

    <footer class="footer">
      <p class="hat-text-centered">Copyright (c) 2024</p>
    </footer>

  </div>
</template>

<script>
export default{
  data(){
    return{
      showMobileMenu: false,
      cart: {
        items: []
      }
    }
  },
  beforeCreate() {
    this.$store.commit('initializeStore')
  },
  mounted() {
    this.cart = this.$store.state.cart
  },
  computed:{
    cartTotalLength(){
      let totalLenght = 0

      for (let i = 0; i < this.cart.items.length; i++){
        totalLenght += this.cart.items[i].quantity
      }

      return totalLenght
    }
  }
}
</script>


<style lang="scss">
@import '../node_modules/bulma';
</style>

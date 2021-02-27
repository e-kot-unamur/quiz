

<style>
  nav {
    display: flex;
    flex-direction: row;
    justify-content: center;
    padding: 10px 0;
    margin-bottom: 30px;
    border-bottom: 1px solid #8DE7EB;
    align-items: center;
  }

  .logoEkot {
    width: 60px;
  }

  .logoInfo {
    position: absolute;
    left: 92%;
    width: 30px;
  }

  .logoContact {
    position: absolute;
    left: 95%;
    width: 30px;
  }

  @media (max-width : 780px) {
    .logoInfo {
      left : 80%;
    }

    .logoContact {
      left: 90%;
    }
  }
</style>

<nav>
  <img src="/logo/logo_blanc.svg" alt="Logo E-kot" class="logoEkot"/>
  <img src="/info.svg" alt="En savoir plus" class="logoInfo"/>
  <img src="/contact.svg" alt="Nous contacter" class="logoContact"/>
</nav>